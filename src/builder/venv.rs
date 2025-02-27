use colored::*;
use indicatif::{ProgressBar, ProgressStyle, MultiProgress};
use regex::Regex;
use std::fs::File;
use std::io::{self, BufRead};
use std::path::Path;
use std::process::Command;
use std::sync::atomic::Ordering;
use std::time::Duration;
use std::collections::HashSet;

use crate::DEBUG;

pub fn create(script_path: &str, user_imports: Option<Vec<String>>) -> io::Result<()> {
    let multi_progress = MultiProgress::new();
    let spinner_style = ProgressStyle::with_template("{spinner:.green} {msg}")
        .unwrap()
        .tick_chars("⠋⠙⠹⠸⠼⠴⠦⠧⠇⠏");

    let imports_spinner = multi_progress.add(ProgressBar::new_spinner());
    imports_spinner.set_style(spinner_style.clone());
    imports_spinner.set_message("[1/3] 🔍 Scanning imports...");

    let mut imports = scan_imports(script_path, &imports_spinner)?;
    if let Some(user_specified_imports) = user_imports {
        imports.extend(user_specified_imports);
    }
    imports = manage_imports(imports);
    imports_spinner.finish_and_clear();
    println!("[1/3] 🔍 Scanning finished ✅");
    println!("  🔍 {}: {}", "Scanned imports".blue(), imports.join(", ").blue());

    let venv_spinner = multi_progress.add(ProgressBar::new_spinner());
    venv_spinner.set_style(spinner_style.clone());
    venv_spinner.set_message("[2/3] 🌐 Creating virtual environment...");

    create_venv(&venv_spinner)?;
    venv_spinner.finish_and_clear();
    println!("[2/3] 🌐 Virtual environment ready ✅");

    install_packages(&imports, &multi_progress)?;
    Ok(())
}

fn scan_imports(script_path: &str, spinner: &ProgressBar) -> io::Result<Vec<String>> {
    let file = File::open(script_path)?;
    let reader = io::BufReader::new(file);
    let import_regex = Regex::new(r"^(?:from\s+(\S+)\s+import|import\s+(\S+))").unwrap();
    let mut imports = Vec::new();

    for line in reader.lines() {
        let line = line?;
        if let Some(captures) = import_regex.captures(&line) {
            if let Some(import) = captures.get(1).or_else(|| captures.get(2)) {
                imports.push(import.as_str().to_string());
            }
        }
        spinner.tick();
    }

    Ok(imports)
}

fn manage_imports(imports: Vec<String>) -> Vec<String> {
    let mut managed_imports = HashSet::new();
    
    for import in imports {
        match import.as_str() {
            "win32api" | "win32gui" | "win32con" | "win32serviceutil" | "win32service" | "win32event" => {
                managed_imports.insert("pywin32".to_string());
            },
            "cv2" => {
                managed_imports.insert("opencv-python".to_string());
            },
            "git" => {
                managed_imports.insert("GitPython".to_string());
            },
            _ => {
                managed_imports.insert(import);
            }
        }
    }
    
    managed_imports.insert("pyinstaller".to_string());
    
    managed_imports.into_iter().collect()
}

fn create_venv(spinner: &ProgressBar) -> io::Result<()> {
    let output = Command::new("python")
        .args(["-m", "venv", "venv"])
        .output()?;

    if !output.status.success() {
        spinner.finish_with_message("[2/3] 🌐 Virtual environment creation failed ❌");
        return Err(io::Error::new(
            io::ErrorKind::Other,
            format!(
                "Failed to create venv: {}",
                String::from_utf8_lossy(&output.stderr)
            ),
        ));
    }

    Ok(())
}

fn install_packages(imports: &[String], multi_progress: &MultiProgress) -> io::Result<()> {
    let progress_style = ProgressStyle::with_template(
        "[3/3] {msg} {spinner:.green} [{bar:40.cyan/blue}] {pos}/{len}"
    )
    .unwrap()
    .progress_chars("#>-");

    let progress_bar = multi_progress.add(ProgressBar::new(imports.len() as u64));
    progress_bar.set_style(progress_style);
    progress_bar.set_message("📦 Installing packages...");

    let venv_pip = if cfg!(windows) {
        Path::new("venv").join("Scripts").join("pip.exe")
    } else {
        Path::new("venv").join("bin").join("pip")
    };

    let mut successful_installs = 0;
    let mut failed_installs = Vec::new();
    let mut skipped_packages = Vec::new();

    let builtin_packages = vec![
        "random", "time", "sys", "os", "math", "datetime", "collections",
        "itertools", "functools", "re", "json", "csv", "pickle", "sqlite3",
        "xml", "html", "urllib", "http", "socket", "email", "threading",
        "multiprocessing", "asyncio", "typing", "pathlib", "shutil",
    ];

    for package in imports {
        progress_bar.set_message(format!("📦 Processing {:<30}", package));
        
        if builtin_packages.contains(&package.as_str()) {
            skipped_packages.push(package.clone());
            progress_bar.inc(1);
            continue;
        }

        let output = Command::new(&venv_pip)
            .args(["install", "--upgrade", package])
            .output()?;
        
        if output.status.success() {
            successful_installs += 1;
        } else {
            eprintln!("\n{}", String::from_utf8_lossy(&output.stderr).red());
            eprintln!(
                "❌ {} Failed to install package: {}",
                "Error:".red(),
                package
            );
            if DEBUG.load(Ordering::SeqCst) {
                eprintln!("🔍 {}: {}", "Debug".blue(), String::from_utf8_lossy(&output.stderr));
            }
            failed_installs.push(package.clone());
        }

        progress_bar.inc(1);
        std::thread::sleep(Duration::from_millis(100)); // Slow down for visual effect
    }

    progress_bar.finish_and_clear();

    if failed_installs.is_empty() && skipped_packages.is_empty() {
        println!("[3/3] 📦 All packages installed successfully ✅");
    } else {
        println!("[3/3] 📦 {}/{} packages installed successfully ✅", successful_installs, imports.len() - skipped_packages.len());
        if !skipped_packages.is_empty() {
            println!("ℹ️  {} The following built-in packages were skipped:", "Info:".blue());
            for package in &skipped_packages {
                println!("   - {}", package);
            }
        }
        if !failed_installs.is_empty() {
            println!("⚠️  {} The following packages failed to install:", "Warning:".yellow());
            for package in &failed_installs {
                println!("   - {}", package);
            }
        }
    }

    Ok(())
}

use colored::*;
use regex::Regex;
use std::fs::File;
use std::io::{self, BufRead};
use std::path::Path;
use std::process::Command;
use std::sync::atomic::Ordering;

use crate::DEBUG;

pub fn create(script_path: &str) -> io::Result<()> {
    let imports = scan_imports(script_path)?;
    create_venv()?;
    install_packages(&imports)?;
    Ok(())
}

fn scan_imports(script_path: &str) -> io::Result<Vec<String>> {
    println!("[!] Scanning script for imports...");
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
    }

    if DEBUG.load(Ordering::SeqCst) {
        println!("[!] Debug: Scanned imports: {:?}", imports);
    }

    println!("[{}] Found imports: {}", "OK".green(), imports.join(", ").blue());

    Ok(imports)
}

fn create_venv() -> io::Result<()> {
    println!("[!] Creating virtual environment...");
    let output = Command::new("python")
        .args(["-m", "venv", "venv"])
        .output()?;

    if !output.status.success() {
        return Err(io::Error::new(
            io::ErrorKind::Other,
            format!(
                "Failed to create venv: {}",
                String::from_utf8_lossy(&output.stderr)
            ),
        ));
    }

    println!("[{}] Virtual environment created successfully", "OK".green());
    Ok(())
}

fn install_packages(imports: &[String]) -> io::Result<()> {
    println!("[!] Installing packages...");
    let venv_pip = if cfg!(windows) {
        Path::new("venv").join("Scripts").join("pip.exe")
    } else {
        Path::new("venv").join("bin").join("pip")
    };

    for package in imports {
        println!("[!] Installing package: {}", package);
        let output = Command::new(&venv_pip)
            .args(["install", "--upgrade", package])
            .output()?;
        
        println!("{}", String::from_utf8_lossy(&output.stdout));

        if !output.status.success() {
            println!("{}", String::from_utf8_lossy(&output.stderr).red());
            eprintln!(
                "[{}] Failed to install package: {}",
                "ERROR".red(),
                package
            );
            if DEBUG.load(Ordering::SeqCst) {
                eprintln!("[!] Debug: {}", String::from_utf8_lossy(&output.stderr));
            }
        } else {
            println!(
                "[{}] Successfully installed package: {}",
                "OK".green(),
                package
            );
        }
    }

    Ok(())
}

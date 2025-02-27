use std::fs;
use std::io;
use std::path::Path;
use colored::*;
use indicatif::{ProgressBar, ProgressStyle, MultiProgress};

pub fn clean(dir_path: &str, script_name: &str, custom_name: Option<&str>, custom_args: Option<&[String]>) -> io::Result<()> {
    let multi_progress = MultiProgress::new();
    let spinner_style = ProgressStyle::with_template("{spinner:.green} {msg}")
        .unwrap()
        .tick_chars("⠋⠙⠹⠸⠼⠴⠦⠧⠇⠏");

    let cleaning_spinner = multi_progress.add(ProgressBar::new_spinner());
    cleaning_spinner.set_style(spinner_style.clone());
    cleaning_spinner.set_message("🧹 Starting cleaning process...");

    let name = custom_name.unwrap_or(script_name).replace(".py", "").replace(".exe", "");

    let dist = format!("{}.dist", name);
    let build = format!("{}.build", name);
    let onefile_dist = format!("{}.onefile-dist", name);
    let onefile_build = format!("{}.onefile-build", name);
    let spec = format!("{}.spec", name);

    let directories_to_clean = vec![
        "build",
        "dist",
        "venv",
        "__pycache__",
        &dist,
        &build,
        &onefile_dist,
        &onefile_build,
    ];

    let files_to_remove = vec![
        &spec,
    ];

    // Clean directories
    for dir in directories_to_clean {
        let path = Path::new(dir_path).join(dir);
        if path.exists() {
            cleaning_spinner.set_message(format!("🗑️  Cleaning {} directory", dir.blue()));
            match fs::remove_dir_all(&path) {
                Ok(_) => println!("  -> 🧹 Cleaned {} directory", dir.blue()),
                Err(e) => eprintln!("  -> {} Failed to clean {} directory: {}", "❌ Error:".red(), dir, e),
            }
        }
        cleaning_spinner.tick();
    }

    // Remove files
    for file in files_to_remove {
        let path = Path::new(dir_path).join(file);
        if path.exists() {
            cleaning_spinner.set_message(format!("🗑️  Removing {} file", file.blue()));
            match fs::remove_file(&path) {
                Ok(_) => println!("  -> 🧹 Removed {} file", file.blue()),
                Err(e) => eprintln!("  -> {} Failed to remove {} file: {}", "❌ Error:".red(), file, e),
            }
        }
        cleaning_spinner.tick();
    }

    // Handle --onedir custom argument
    if let Some(args) = custom_args {
        if args.contains(&"--onedir".to_string()) {
            println!("  -> 🔍 Detected --onedir argument, skipping dist directory cleanup");
        }
    }

    cleaning_spinner.finish_with_message("✅ Cleaning process completed");
    Ok(())
}

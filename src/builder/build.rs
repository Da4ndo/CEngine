use std::process::Command;
use std::path::Path;
use std::io;
use colored::*;

use crate::DEBUG;

pub fn build(script_path: &str, name: &str, custom_args: &[String]) -> io::Result<()> {
    println!("[!] Starting PyInstaller build process...");

    // Determine the correct path to pyinstaller executable
    let pyinstaller_path = if cfg!(windows) {
        Path::new("venv").join("Scripts").join("pyinstaller.exe")
    } else {
        Path::new("venv").join("bin").join("pyinstaller")
    };

    // Construct PyInstaller command
    let mut command = Command::new(pyinstaller_path);
    command.arg("--onefile")
           .arg("--name")
           .arg(name)
           .args(custom_args)
           .arg(script_path);

    // Execute PyInstaller
    let output = command.output()?;

    if !output.status.success() {
        eprintln!("[{}] PyInstaller build failed", "ERROR".red());
        if DEBUG.load(std::sync::atomic::Ordering::SeqCst) {
            eprintln!("[!] Debug: {}", String::from_utf8_lossy(&output.stderr));
        }
        return Err(io::Error::new(io::ErrorKind::Other, "PyInstaller build failed"));
    }

    println!("[{}] PyInstaller build completed successfully", "OK".green());

    // Move the generated executable
    let source_path = Path::new("dist").join(name);
    let dest_path = Path::new(name);

    if let Err(e) = std::fs::rename(&source_path, &dest_path) {
        eprintln!("[{}] Failed to move executable: {}", "WARNING".yellow(), e);
        println!("[!] Executable location: {:?}", source_path);
    } else {
        println!("[{}] Executable moved to: {:?}", "OK".green(), dest_path);
    }

    // Clean up build artifacts
    clean_build_artifacts()?;

    Ok(())
}

fn clean_build_artifacts() -> io::Result<()> {
    println!("[!] Cleaning up build artifacts...");

    let dirs_to_remove = ["build", "dist", "__pycache__"];
    let files_to_remove = [".spec"];

    for dir in &dirs_to_remove {
        if let Err(e) = std::fs::remove_dir_all(dir) {
            if e.kind() != io::ErrorKind::NotFound {
                eprintln!("[{}] Failed to remove directory {}: {}", "WARNING".yellow(), dir, e);
            }
        } else {
            println!("[{}] Removed directory: {}", "OK".green(), dir);
        }
    }

    for file in &files_to_remove {
        if let Err(e) = std::fs::remove_file(file) {
            if e.kind() != io::ErrorKind::NotFound {
                eprintln!("[{}] Failed to remove file {}: {}", "WARNING".yellow(), file, e);
            }
        } else {
            println!("[{}] Removed file: {}", "OK".green(), file);
        }
    }

    Ok(())
}

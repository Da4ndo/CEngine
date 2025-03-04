use std::process::Command;
use std::path::Path;
use std::io;
use colored::*;
use std::sync::atomic::Ordering;

use crate::DEBUG;

pub fn build(script_path: &str, name: &str, custom_args: &[String]) -> io::Result<String> {
    let debug = DEBUG.load(Ordering::SeqCst);
    
    println!("[!] Starting PyInstaller build process...");

    // Determine the correct path to pyinstaller executable
    let pyinstaller_path = if cfg!(windows) {
        Path::new("venv").join("Scripts").join("pyinstaller.exe")
    } else {
        Path::new("venv").join("bin").join("pyinstaller")
    };

    if debug {
        println!(":: Debug: PyInstaller path: {:?}", pyinstaller_path);
    }

    // Construct PyInstaller command
    let mut command = Command::new(&pyinstaller_path);
    command.arg("--onefile")
           .arg("--name")
           .arg(name)
           .args(custom_args)
           .arg(script_path);

    if debug {
        println!(":: Debug: PyInstaller command: {:?}", command);
    }

    // Execute PyInstaller
    let output = command.output()?;

    if !output.status.success() {
        eprintln!("[{}] PyInstaller build failed", "ERROR".red());
        if debug {
            eprintln!(":: Debug: PyInstaller stderr: {}", String::from_utf8_lossy(&output.stderr));
            eprintln!(":: Debug: PyInstaller stdout: {}", String::from_utf8_lossy(&output.stdout));
        }
        return Err(io::Error::other("PyInstaller build failed"));
    }

    println!("[{}] PyInstaller build completed successfully", "OK".green());

    // Move the generated executable
    let source_path = Path::new("dist").join(name);
    let dest_path = Path::new(name);

    if debug {
        println!(":: Debug: Moving executable from {:?} to {:?}", source_path, dest_path);
    }

    let output_path = if cfg!(windows) {
        format!("{}.exe", dest_path.display())
    } else {
        dest_path.display().to_string()
    };

    if let Err(e) = std::fs::rename(&source_path, dest_path) {
        eprintln!("[{}] Failed to move executable: {}", "WARNING".yellow(), e);
        println!("[!] Executable location: {:?}", source_path);
        if debug {
            eprintln!(":: Debug: Error moving executable: {:?}", e);
        }
        // Return the source path if we couldn't move it
        Ok(source_path.display().to_string())
    } else {
        println!("[{}] Executable moved to: {:?}", "OK".green(), dest_path);
        Ok(output_path)
    }
}
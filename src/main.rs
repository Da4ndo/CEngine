use clap::{Command, Arg};
use std::process;
use colored::*;
use std::sync::atomic::{AtomicBool, Ordering};
use comfy_table::{Table, presets::UTF8_FULL, modifiers::UTF8_ROUND_CORNERS, Cell, Color};

mod builder;

static DEBUG: AtomicBool = AtomicBool::new(false);
static FORCE: AtomicBool = AtomicBool::new(false);

fn main() {
    let app = Command::new("cengine")
        .version(env!("CARGO_PKG_VERSION"))
        .author("Da4ndo <contact@da4ndo.com>")
        .about("CEngine (Convert Engine) is an open-source converter for Python to create exe from py files.")
        .arg_required_else_help(true)
        .color(clap::ColorChoice::Always)
        .arg(Arg::new("script")
            .short('s')
            .long("script")
            .alias("file")
            .value_name("SCRIPT")
            .required(true)
            .help("Define a script to be made into an executable"))
        .arg(Arg::new("name")
            .short('n')
            .long("name")
            .value_name("NAME")
            .help("Define the script name"))
        .arg(Arg::new("add-imports")
            .long("add-imports")
            .value_name("IMPORTS")
            .num_args(1..)
            .help("Add more imports"))
        .arg(Arg::new("force-platform")
            .long("force-platform")
            .value_name("PLATFORM")
            .help("Add custom arguments"))
        .arg(Arg::new("clean")
            .long("clean")
            .action(clap::ArgAction::SetTrue)
            .help("Clean failed builds"))
        .arg(Arg::new("debug")
            .long("debug")
            .global(true)
            .action(clap::ArgAction::SetTrue)
            .help("Sets the debug environment to true"))
        .arg(Arg::new("force")
            .long("force")
            .global(true)
            .action(clap::ArgAction::SetTrue)
            .help("Forces the operation to proceed with all warnings and skippings"));

    let matches = app.clone().try_get_matches().unwrap_or_else(|e| {
        match e.kind() {
            clap::error::ErrorKind::UnknownArgument | clap::error::ErrorKind::InvalidSubcommand => {
                eprintln!("{} {}", ":: Error:".red(), e.to_string().red());
            },
            _ => {
                println!("{}", e);
            }
        }
        process::exit(1);
    });

    if matches.get_flag("debug") {
        DEBUG.store(true, Ordering::SeqCst);
        println!("{} Debug mode is activated.", ":: Debug:".blue());
    }

    if matches.get_flag("force") {
        FORCE.store(true, Ordering::SeqCst);
        println!("{} Force mode is activated.", ":: Debug:".blue());
    }

    if DEBUG.load(Ordering::SeqCst) {
        if cfg!(debug_assertions) {
            println!("{} Application is running in debug build mode.", ":: Debug:".blue());
        } else {
            println!("{} Application is running in release build mode.", ":: Debug:".blue());
        }
    }

    banner();

    let mut table = Table::new();
    table.load_preset(UTF8_FULL)
        .apply_modifier(UTF8_ROUND_CORNERS)
        .set_header(vec![
            Cell::new("Category").fg(Color::Yellow),
            Cell::new("Information").fg(Color::Yellow)
        ]);

    table.add_row(vec![
        Cell::new("OS").fg(Color::Green),
        Cell::new(std::env::consts::OS).fg(Color::Cyan)
    ]);
    table.add_row(vec![
        Cell::new("Architecture").fg(Color::Green),
        Cell::new(std::env::consts::ARCH).fg(Color::Cyan)
    ]);

    let script_path = matches.get_one::<String>("script").unwrap();
    table.add_row(vec![
        Cell::new("Script Path").fg(Color::Green),
        Cell::new(script_path).fg(Color::Cyan)
    ]);

    if let Ok(canonical_path) = std::fs::canonicalize(script_path) {
        table.add_row(vec![
            Cell::new("Canonical Path").fg(Color::Green),
            Cell::new(&canonical_path.display().to_string()).fg(Color::Cyan)
        ]);
    }

    if let Ok(metadata) = std::fs::metadata(script_path) {
        table.add_row(vec![
            Cell::new("File Size").fg(Color::Green),
            Cell::new(&format!("{} bytes", metadata.len())).fg(Color::Cyan)
        ]);
        if let Ok(modified) = metadata.modified() {
            if let Ok(modified_str) = modified.duration_since(std::time::UNIX_EPOCH) {
                table.add_row(vec![
                    Cell::new("Last Modified").fg(Color::Green),
                    Cell::new(&format!("{} seconds since UNIX epoch", modified_str.as_secs())).fg(Color::Cyan)
                ]);
            }
        }
    }

    table.add_row(vec![
        Cell::new("Debug Mode").fg(Color::Green),
        Cell::new(&DEBUG.load(Ordering::SeqCst).to_string()).fg(Color::Cyan)
    ]);
    table.add_row(vec![
        Cell::new("Force Mode").fg(Color::Green),
        Cell::new(&FORCE.load(Ordering::SeqCst).to_string()).fg(Color::Cyan)
    ]);

    println!("{}", table);

    match builder::venv::create(matches.get_one::<String>("script").unwrap()) {
        Ok(_) => println!("{} Virtual environment created successfully", ":: OK:".green()),
        Err(e) => eprintln!("{} Failed to create virtual environment: {}", ":: Error:".red(), e.to_string().red()),
    }

    // Here you would implement the main logic for CEngine
    // For example:
    // if matches.get_flag("clean") {
    //     commands::clean(&matches);
    // } else if let Some(script) = matches.get_one::<String>("script") {
    //     commands::convert(script, &matches);
    // } else {
    //     println!("{} For command usage, type --help", ":: Info:".bright_blue());
    // }

    // use loading, moving, animted logs for logging also use new prefix, think of a complteletty new. Eg.: dots moving at the end and on finish text changes to finshed and we have thick also. so use emojies, colored words in the text, etc. Maybe also use spacing, new lines to make readabilty better
}

fn banner() {
    let banner_text = r#"
          |middle|
  /$$$$$$ |middle| /$$$$$$$$                     /$$                    
 /$$__  $$|middle|| $$_____/                    |__/                    
| $$  \__/|middle|| $$       /$$$$$$$   /$$$$$$  /$$ /$$$$$$$   /$$$$$$ 
| $$      |middle|| $$$$$   | $$__  $$ /$$__  $$| $$| $$__  $$ /$$__  $$
| $$      |middle|| $$__/   | $$  \ $$| $$  \ $$| $$| $$  \ $$| $$$$$$$$
| $$    $$|middle|| $$      | $$  | $$| $$  | $$| $$| $$  | $$| $$_____/
|  $$$$$$/|middle|| $$$$$$$$| $$  | $$|  $$$$$$$| $$| $$  | $$|  $$$$$$$
 \______/ |middle||________/|__/  |__/ \____  $$|__/|__/  |__/ \_______/
          |middle|                     /$$  \ $$                        
          |middle|                    |  $$$$$$/                        
          |middle|                     \______/                                                       
    "#;
    println!();
    for line in banner_text.trim().lines() {
        let parts: Vec<&str> = line.split("|middle|").collect();
        if parts.len() == 2 {
            println!("{}{}", parts[0].yellow(), parts[1].blue());
        }
    }
    println!();
    let version_info = format!("CEngine Version: {}{}", "v".blue(), env!("CARGO_PKG_VERSION").blue());
    let border_length = version_info.len() - 15; // -23 because of colors
    let border = "═".repeat(border_length).yellow();
    println!("{}", border);
    println!("{} {} {}", "║".yellow(), version_info, "║".yellow());
    println!("{}", border);
    println!();
}
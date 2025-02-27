use chrono::DateTime;
use clap::{Arg, Command};
use colored::*;
use comfy_table::{modifiers::UTF8_ROUND_CORNERS, presets::UTF8_FULL, Cell, Color, Table};
use std::fs;
use std::path::Path;
use std::sync::atomic::{AtomicBool, Ordering};

mod builder;
mod clean;

static DEBUG: AtomicBool = AtomicBool::new(false);
static FORCE: AtomicBool = AtomicBool::new(false);

fn main() {
    let matches = create_cli().get_matches();

    set_global_flags(&matches);
    print_debug_info();

    banner();

    let script_path = matches.get_one::<String>("script").unwrap();
    info_table(script_path);

    let additional_imports = matches
        .get_many::<String>("add-imports")
        .map(|imports| imports.cloned().collect());

    handle_venv_creation(script_path, additional_imports);

    let name = get_output_name(&matches, script_path);
    let custom_args: Vec<String> = matches
        .get_many::<String>("")
        .map(|vals| vals.map(|s| s.to_string()).collect())
        .unwrap_or_default();

    if DEBUG.load(Ordering::Relaxed) {
        println!("Custom args: {}", custom_args.join(" "));
    }

    let absolute_script_path = fs::canonicalize(script_path)
        .expect("Failed to get absolute path")
        .to_str()
        .expect("Failed to convert path to string")
        .to_string();

    let output_path = handle_build(&absolute_script_path, &name, &custom_args);
    
    // Call clean after build
    let dir_path = Path::new(&absolute_script_path).parent().unwrap().to_str().unwrap();
    if let Err(e) = clean::clean(dir_path, script_path, Some(&name), Some(&custom_args)) {
        eprintln!("{} Failed to clean: {}", ":: Error:".red(), e.to_string().red());
    }

    // Print final output path if build was successful
    if let Some(path) = output_path {
        // Convert absolute path to relative path
        let current_dir = std::env::current_dir().unwrap();
        let path = Path::new(&path);
        let relative_path = pathdiff::diff_paths(path, current_dir)
            .unwrap_or_else(|| path.to_path_buf())
            .display()
            .to_string();
        
        println!("\n\n{} {}", "📦 OUTPUT →".red().bold(), format!("./{}", relative_path).bold());
    }
}

fn create_cli() -> Command {
    Command::new("cengine")
        .version(env!("CARGO_PKG_VERSION"))
        .author("Da4ndo <contact@da4ndo.com>")
        .about("CEngine (Convert Engine) is an open-source converter for Python to create exe from py files.")
        .arg_required_else_help(true)
        .color(clap::ColorChoice::Always)
        .arg(Arg::new("script")
            .alias("file")
            .value_name("SCRIPT")
            .help("Define a script to be made into an executable")
            .index(1))
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
            .help("Forces the operation to proceed with all warnings and skippings"))
        .allow_external_subcommands(true)
        .allow_hyphen_values(true)
}

fn set_global_flags(matches: &clap::ArgMatches) {
    if matches.get_flag("debug") {
        DEBUG.store(true, Ordering::SeqCst);
        println!("{} Debug mode is activated.", ":: Debug:".blue());
    }

    if matches.get_flag("force") {
        FORCE.store(true, Ordering::SeqCst);
        println!("{} Force mode is activated.", ":: Debug:".blue());
    }
}

fn print_debug_info() {
    if DEBUG.load(Ordering::SeqCst) {
        let mode = if cfg!(debug_assertions) {
            "debug"
        } else {
            "release"
        };
        println!(
            "{} Application is running in {} build mode.",
            ":: Debug:".blue(),
            mode
        );
    }
}

fn handle_venv_creation(script_path: &str, additional_imports: Option<Vec<String>>) {
    match builder::venv::create(script_path, additional_imports) {
        Ok(_) => println!(
            "[{}] Virtual environment created successfully",
            "OK".green()
        ),
        Err(e) => eprintln!(
            "{} Failed to create virtual environment: {}",
            ":: Error:".red(),
            e.to_string().red()
        ),
    }
}

fn get_output_name(matches: &clap::ArgMatches, script_path: &str) -> String {
    matches
        .get_one::<String>("name")
        .cloned()
        .unwrap_or_else(|| {
            let file_name = Path::new(script_path)
                .file_stem()
                .unwrap()
                .to_str()
                .unwrap();
            let current_time = chrono::Local::now().format("%Y%m%d_%H%M%S");
            format!("{}_{}", file_name, current_time)
        })
}

fn handle_build(absolute_script_path: &str, name: &str, custom_args: &[String]) -> Option<String> {
    match builder::build::build(absolute_script_path, name, custom_args) {
        Ok(output_path) => {
            println!("{}\n", "[OK] Executable built successfully".green().bold());
            Some(output_path)
        },
        Err(e) => {
            eprintln!(
                "{} Failed to build executable: {}",
                ":: Error:".red(),
                e.to_string().red()
            );
            None
        },
    }
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
    let version_info = format!(
        "CEngine Version: {}{}",
        "v".blue(),
        env!("CARGO_PKG_VERSION").blue()
    );
    let border_length = version_info.len() - 14; // -14 because of colors
    let border = "═".repeat(border_length).yellow();
    println!(
        "{}\n{} {} {}\n{}\n",
        border,
        "║".yellow(),
        version_info,
        "║".yellow(),
        border
    );
}

fn info_table(script_path: &str) {
    let mut table = Table::new();
    table
        .load_preset(UTF8_FULL)
        .apply_modifier(UTF8_ROUND_CORNERS)
        .set_header(vec![
            Cell::new("Category").fg(Color::Yellow),
            Cell::new("Information").fg(Color::Yellow),
        ]);

    add_row(&mut table, "OS", std::env::consts::OS);
    add_row(&mut table, "Architecture", std::env::consts::ARCH);
    add_row(&mut table, "Script Path", script_path);

    if let Ok(canonical_path) = fs::canonicalize(script_path) {
        add_row(
            &mut table,
            "Canonical Path",
            canonical_path.display().to_string(),
        );
    }

    if let Ok(metadata) = fs::metadata(script_path) {
        add_row(&mut table, "File Size", format!("{} bytes", metadata.len()));
        if let Ok(modified) = metadata.modified() {
            if let Some(datetime) = DateTime::from_timestamp(
                modified
                    .duration_since(std::time::UNIX_EPOCH)
                    .unwrap()
                    .as_secs() as i64,
                0,
            ) {
                add_row(
                    &mut table,
                    "Last Modified",
                    datetime.format("%Y-%m-%d %H:%M:%S").to_string(),
                );
            }
        }
    }

    add_row(
        &mut table,
        "Debug Mode",
        DEBUG.load(Ordering::SeqCst).to_string(),
    );
    add_row(
        &mut table,
        "Force Mode",
        FORCE.load(Ordering::SeqCst).to_string(),
    );

    println!("{}\n", table);
}

fn add_row(table: &mut Table, category: &str, info: impl AsRef<str>) {
    table.add_row(vec![
        Cell::new(category).fg(Color::Green),
        Cell::new(info.as_ref()).fg(Color::Cyan),
    ]);
}

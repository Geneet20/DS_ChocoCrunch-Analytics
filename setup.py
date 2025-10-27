"""
ChocoCrunch Analytics - Quick Setup Script
Automated environment setup and dependency installation
"""

import os
import sys
import subprocess
import platform

def check_python_version():
    """Check if Python version is compatible"""
    print("🐍 Checking Python version...")
    version = sys.version_info
    
    if version.major < 3 or (version.major == 3 and version.minor < 8):
        print("❌ Python 3.8 or higher is required")
        print(f"   Current version: {version.major}.{version.minor}.{version.micro}")
        return False
    
    print(f"✅ Python {version.major}.{version.minor}.{version.micro} detected")
    return True

def create_virtual_environment():
    """Create virtual environment for the project"""
    print("🏗️ Creating virtual environment...")
    
    try:
        venv_name = "choco_env"
        subprocess.run([sys.executable, "-m", "venv", venv_name], check=True)
        print(f"✅ Virtual environment '{venv_name}' created successfully")
        
        # Provide activation instructions
        if platform.system() == "Windows":
            activation_cmd = f"{venv_name}\\Scripts\\activate"
        else:
            activation_cmd = f"source {venv_name}/bin/activate"
        
        print(f"📝 To activate: {activation_cmd}")
        return True
        
    except subprocess.CalledProcessError as e:
        print(f"❌ Failed to create virtual environment: {e}")
        return False

def install_dependencies():
    """Install required Python packages"""
    print("📦 Installing dependencies...")
    
    try:
        # Check if we're in a virtual environment
        if hasattr(sys, 'real_prefix') or (hasattr(sys, 'base_prefix') and sys.base_prefix != sys.prefix):
            print("✅ Virtual environment detected")
        else:
            print("⚠️ Warning: Not in a virtual environment")
        
        # Install requirements
        requirements_file = "requirements.txt"
        if os.path.exists(requirements_file):
            result = subprocess.run([
                sys.executable, "-m", "pip", "install", "-r", requirements_file
            ], capture_output=True, text=True)
            
            if result.returncode == 0:
                print("✅ All dependencies installed successfully")
                return True
            else:
                print(f"❌ Failed to install dependencies: {result.stderr}")
                return False
        else:
            print(f"❌ Requirements file not found: {requirements_file}")
            return False
            
    except Exception as e:
        print(f"❌ Error installing dependencies: {e}")
        return False

def verify_installation():
    """Verify that key packages are installed correctly"""
    print("🔍 Verifying installation...")
    
    required_packages = [
        "pandas", "numpy", "requests", "matplotlib", 
        "seaborn", "plotly", "streamlit", "jupyter"
    ]
    
    failed_imports = []
    
    for package in required_packages:
        try:
            __import__(package)
            print(f"✅ {package}")
        except ImportError:
            failed_imports.append(package)
            print(f"❌ {package}")
    
    if failed_imports:
        print(f"\\n⚠️ Failed to import: {', '.join(failed_imports)}")
        return False
    else:
        print("\\n🎉 All packages verified successfully!")
        return True

def create_project_directories():
    """Create necessary project directories"""
    print("📁 Creating project directories...")
    
    directories = [
        "data/raw",
        "data/processed", 
        "data/database",
        "visualizations/exports",
        "logs"
    ]
    
    for directory in directories:
        os.makedirs(directory, exist_ok=True)
        print(f"✅ Created: {directory}")
    
    return True

def main():
    """Main setup function"""
    print("🍫✨ ChocoCrunch Analytics - Project Setup")
    print("=" * 50)
    
    # Check Python version
    if not check_python_version():
        return False
    
    # Create directories
    if not create_project_directories():
        return False
    
    # Install dependencies (assuming user is in correct environment)
    if not install_dependencies():
        print("\\n⚠️ Dependency installation failed")
        print("💡 Try running: pip install -r requirements.txt")
        return False
    
    # Verify installation
    if not verify_installation():
        print("\\n⚠️ Package verification failed")
        return False
    
    # Success message
    print("\\n" + "=" * 50)
    print("🎉 Setup completed successfully!")
    print("\\n🚀 Next steps:")
    print("  1. Run the complete pipeline: python run_project.py")
    print("  2. Or run individual components:")
    print("     • Extract data: python src/data_extraction.py")
    print("     • Launch dashboard: streamlit run streamlit_app/app.py")
    print("  3. Open analysis notebooks: jupyter notebook notebooks/")
    print("\\n📊 Ready to analyze chocolate market data!")
    
    return True

if __name__ == "__main__":
    success = main()
    sys.exit(0 if success else 1)
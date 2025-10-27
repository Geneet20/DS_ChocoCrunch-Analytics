"""
ChocoCrunch Analytics - Project Execution Script
Main script to run the complete data analysis pipeline
"""

import os
import sys
import subprocess
import logging
from datetime import datetime

# Setup logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler('project_execution.log'),
        logging.StreamHandler()
    ]
)
logger = logging.getLogger(__name__)

class ChocoCrunchPipeline:
    """
    Complete data analysis pipeline for ChocoCrunch Analytics
    """
    
    def __init__(self):
        self.project_root = os.path.dirname(os.path.abspath(__file__))
        self.steps_completed = []
        self.errors = []
        
    def log_step(self, step_name, success=True, error_msg=""):
        """Log completion of pipeline steps"""
        if success:
            self.steps_completed.append(step_name)
            logger.info(f"✅ {step_name} completed successfully")
        else:
            self.errors.append(f"{step_name}: {error_msg}")
            logger.error(f"❌ {step_name} failed: {error_msg}")
    
    def run_data_extraction(self):
        """Step 1: Extract data from OpenFoodFacts API"""
        try:
            logger.info("🍫 Starting data extraction from OpenFoodFacts API...")
            
            # Check if raw data already exists
            raw_data_path = os.path.join(self.project_root, "data", "raw", "chocolate_products_raw.csv")
            
            if os.path.exists(raw_data_path):
                logger.info("📁 Raw data already exists, skipping extraction")
                self.log_step("Data Extraction")
                return True
            
            # Run data extraction script
            extraction_script = os.path.join(self.project_root, "src", "data_extraction.py")
            
            if os.path.exists(extraction_script):
                result = subprocess.run([sys.executable, extraction_script], 
                                      capture_output=True, text=True, cwd=self.project_root)
                
                if result.returncode == 0:
                    self.log_step("Data Extraction")
                    return True
                else:
                    self.log_step("Data Extraction", False, result.stderr)
                    return False
            else:
                self.log_step("Data Extraction", False, "Extraction script not found")
                return False
                
        except Exception as e:
            self.log_step("Data Extraction", False, str(e))
            return False
    
    def run_data_cleaning(self):
        """Step 2: Clean and preprocess data"""
        try:
            logger.info("🧹 Starting data cleaning and preprocessing...")
            
            # Check if cleaned data already exists
            cleaned_data_path = os.path.join(self.project_root, "data", "processed", "chocolate_products_cleaned.csv")
            
            if os.path.exists(cleaned_data_path):
                logger.info("📁 Cleaned data already exists, skipping cleaning")
                self.log_step("Data Cleaning")
                return True
            
            # Run data cleaning script
            cleaning_script = os.path.join(self.project_root, "src", "data_cleaning.py")
            
            if os.path.exists(cleaning_script):
                result = subprocess.run([sys.executable, cleaning_script], 
                                      capture_output=True, text=True, cwd=self.project_root)
                
                if result.returncode == 0:
                    self.log_step("Data Cleaning")
                    return True
                else:
                    self.log_step("Data Cleaning", False, result.stderr)
                    return False
            else:
                self.log_step("Data Cleaning", False, "Cleaning script not found")
                return False
                
        except Exception as e:
            self.log_step("Data Cleaning", False, str(e))
            return False
    
    def run_feature_engineering(self):
        """Step 3: Create derived features and metrics"""
        try:
            logger.info("⚙️ Starting feature engineering...")
            
            # Check if engineered data already exists
            engineered_data_path = os.path.join(self.project_root, "data", "processed", "chocolate_products_engineered.csv")
            
            if os.path.exists(engineered_data_path):
                logger.info("📁 Engineered data already exists, skipping feature engineering")
                self.log_step("Feature Engineering")
                return True
            
            # Run feature engineering script
            engineering_script = os.path.join(self.project_root, "src", "feature_engineering.py")
            
            if os.path.exists(engineering_script):
                result = subprocess.run([sys.executable, engineering_script], 
                                      capture_output=True, text=True, cwd=self.project_root)
                
                if result.returncode == 0:
                    self.log_step("Feature Engineering")
                    return True
                else:
                    self.log_step("Feature Engineering", False, result.stderr)
                    return False
            else:
                self.log_step("Feature Engineering", False, "Engineering script not found")
                return False
                
        except Exception as e:
            self.log_step("Feature Engineering", False, str(e))
            return False
    
    def run_database_setup(self):
        """Step 4: Create database and insert data"""
        try:
            logger.info("🗄️ Starting database setup...")
            
            # Check if database already exists
            db_path = os.path.join(self.project_root, "data", "database", "chococrunch.db")
            
            if os.path.exists(db_path):
                logger.info("📁 Database already exists, skipping setup")
                self.log_step("Database Setup")
                return True
            
            # Run database insertion script
            db_script = os.path.join(self.project_root, "sql", "insert_data.py")
            
            if os.path.exists(db_script):
                result = subprocess.run([sys.executable, db_script], 
                                      capture_output=True, text=True, cwd=self.project_root)
                
                if result.returncode == 0:
                    self.log_step("Database Setup")
                    return True
                else:
                    self.log_step("Database Setup", False, result.stderr)
                    return False
            else:
                self.log_step("Database Setup", False, "Database script not found")
                return False
                
        except Exception as e:
            self.log_step("Database Setup", False, str(e))
            return False
    
    def validate_project_structure(self):
        """Validate that all necessary files and directories exist"""
        try:
            logger.info("🔍 Validating project structure...")
            
            required_dirs = [
                "src", "data", "data/raw", "data/processed", "data/database",
                "sql", "notebooks", "streamlit_app", "visualizations"
            ]
            
            required_files = [
                "src/config.py",
                "src/data_extraction.py", 
                "src/data_cleaning.py",
                "src/feature_engineering.py",
                "sql/schema.sql",
                "sql/queries.sql",
                "sql/insert_data.py",
                "streamlit_app/app.py",
                "requirements.txt",
                "README.md"
            ]
            
            missing_items = []
            
            # Check directories
            for directory in required_dirs:
                dir_path = os.path.join(self.project_root, directory)
                if not os.path.exists(dir_path):
                    missing_items.append(f"Directory: {directory}")
            
            # Check files
            for file_path in required_files:
                full_path = os.path.join(self.project_root, file_path)
                if not os.path.exists(full_path):
                    missing_items.append(f"File: {file_path}")
            
            if missing_items:
                logger.warning(f"Missing items: {missing_items}")
                self.log_step("Project Structure Validation", False, f"Missing: {', '.join(missing_items)}")
                return False
            else:
                self.log_step("Project Structure Validation")
                return True
                
        except Exception as e:
            self.log_step("Project Structure Validation", False, str(e))
            return False
    
    def generate_execution_report(self):
        """Generate comprehensive execution report"""
        try:
            logger.info("📊 Generating execution report...")
            
            report = {
                "execution_timestamp": datetime.now().isoformat(),
                "project_root": self.project_root,
                "steps_completed": self.steps_completed,
                "total_steps": len(self.steps_completed),
                "success_rate": f"{len(self.steps_completed) / 5 * 100:.1f}%",
                "errors": self.errors,
                "next_steps": []
            }
            
            # Generate next steps based on completion
            if "Data Extraction" in self.steps_completed:
                report["next_steps"].append("✅ Data extracted - proceed to analysis")
            else:
                report["next_steps"].append("❌ Run data extraction first")
            
            if "Database Setup" in self.steps_completed:
                report["next_steps"].append("✅ Database ready - execute SQL queries")
            else:
                report["next_steps"].append("❌ Complete database setup")
            
            if len(self.steps_completed) >= 4:
                report["next_steps"].append("✅ Run Streamlit dashboard: streamlit run streamlit_app/app.py")
                report["next_steps"].append("✅ Open EDA notebook for analysis")
            
            # Save report
            import json
            report_path = os.path.join(self.project_root, "execution_report.json")
            with open(report_path, 'w') as f:
                json.dump(report, f, indent=2)
            
            logger.info(f"📄 Execution report saved to: {report_path}")
            
            # Print summary
            print("\n" + "="*80)
            print("🍫 CHOCOCRUNCH ANALYTICS - EXECUTION SUMMARY")
            print("="*80)
            print(f"📅 Execution Date: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
            print(f"📁 Project Root: {self.project_root}")
            print(f"✅ Steps Completed: {len(self.steps_completed)}/5")
            print(f"📊 Success Rate: {len(self.steps_completed) / 5 * 100:.1f}%")
            
            print("\\n📋 Completed Steps:")
            for step in self.steps_completed:
                print(f"  ✅ {step}")
            
            if self.errors:
                print("\\n❌ Errors Encountered:")
                for error in self.errors:
                    print(f"  ❌ {error}")
            
            print("\\n🚀 Next Steps:")
            for step in report["next_steps"]:
                print(f"  {step}")
            
            print("\\n" + "="*80)
            
            self.log_step("Report Generation")
            return True
            
        except Exception as e:
            self.log_step("Report Generation", False, str(e))
            return False
    
    def run_complete_pipeline(self):
        """Execute the complete data analysis pipeline"""
        logger.info("🚀 Starting ChocoCrunch Analytics Pipeline")
        logger.info("="*60)
        
        pipeline_steps = [
            ("Project Structure Validation", self.validate_project_structure),
            ("Data Extraction", self.run_data_extraction),
            ("Data Cleaning", self.run_data_cleaning), 
            ("Feature Engineering", self.run_feature_engineering),
            ("Database Setup", self.run_database_setup)
        ]
        
        for step_name, step_function in pipeline_steps:
            logger.info(f"▶️ Executing: {step_name}")
            success = step_function()
            
            if not success and step_name != "Project Structure Validation":
                logger.error(f"❌ Pipeline stopped at: {step_name}")
                break
        
        # Generate final report
        self.generate_execution_report()
        
        if len(self.steps_completed) >= 4:
            logger.info("🎉 Pipeline execution completed successfully!")
            logger.info("🚀 Ready to run analysis and dashboard!")
        else:
            logger.warning("⚠️ Pipeline completed with errors. Check logs for details.")

def main():
    """Main execution function"""
    print("🍫✨ Welcome to ChocoCrunch Analytics!")
    print("📊 Sweet Stats & Sour Truths - Complete Analysis Pipeline")
    print("="*60)
    
    # Initialize and run pipeline
    pipeline = ChocoCrunchPipeline()
    pipeline.run_complete_pipeline()
    
    print("\\n🏁 Pipeline execution finished!")
    print("📄 Check execution_report.json for detailed results")
    print("📋 Check project_execution.log for detailed logs")

if __name__ == "__main__":
    main()
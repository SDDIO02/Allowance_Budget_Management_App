# Allowance Budget Management App

A comprehensive expense tracking application designed to help users manage their budget and track expenses effectively. Available for Windows/Mac/Linux (PC) and mobile devices (Android & iOS).

---

## Table of Contents
1. [Quick Installation](#quick-installation)
2. [Installation on PC](#installation-on-pc)
3. [Installation on Android](#installation-on-android)
4. [Installation on iOS](#installation-on-ios)
5. [Features](#features)
6. [Usage](#usage)

---

## Quick Installation

### ▶ PC (Windows / Mac / Linux)
1. Install Python:
   https://www.python.org/downloads/

2. Save this file as:
   `expense_tracker.py`

3. Run in terminal:
   ```bash
   python expense_tracker.py
   ```

### ▶ ANDROID
1. Install "Pydroid 3" from Play Store
2. Open app
3. Paste the code from this repository
4. Tap RUN ▶️

### ▶ iOS
1. Install "Pythonista" or "Pyto"
2. Create new script
3. Paste the code from this repository
4. Tap RUN ▶️

### NOTES:
- ✅ No external libraries required
- 💾 Data is saved in "data.json"
- 🔌 Works offline

---

## Installation on PC

### Prerequisites
- **Python 3.8 or higher** installed on your system
- **Git** (optional, for cloning the repository)
- A text editor or IDE (VS Code, PyCharm, etc.)

### Step-by-Step Installation

#### Step 1: Download or Clone the Repository
**Option A: Clone using Git**
```bash
git clone https://github.com/SDDIO02/Allowance_Budget_Management_App.git
cd Allowance_Budget_Management_App
```

**Option B: Download ZIP**
- Visit the repository on GitHub
- Click the green "Code" button → Download ZIP
- Extract the ZIP file to your desired location

#### Step 2: Verify Python Installation
```bash
python --version
# or on Mac/Linux
python3 --version
```
Ensure you have Python 3.8 or higher.

#### Step 3: Run the Application
Navigate to the project directory and run:

**On Windows:**
```bash
python main.py
```

**On Mac/Linux:**
```bash
python3 main.py
```

#### Step 4: Follow the On-Screen Prompts
- Enter your name when prompted
- Use the menu to set budgets and add expenses
- Track your spending in real-time

---

## Installation on Android

### Prerequisites
- Android device running Android 8.0 or higher
- Google Play Store access
- Minimum 50MB free storage

### Step-by-Step Installation

#### Method 1: Using Pydroid 3
1. **Open Google Play Store** on your Android device
2. **Search for "Pydroid 3"** and install it
3. **Copy the code** from this GitHub repository
4. **Open Pydroid 3** and create a new script
5. **Paste the code** into the editor
6. **Tap the RUN button (▶️)** to execute

#### Method 2: Using Google Play Store
- Open **Google Play Store** on your Android device
- Search for "Allowance Budget Management App"
- Tap the **Install** button
- Wait for the app to download and install

#### Method 3: Manual APK Installation
If the app is not yet on Play Store:

1. **Enable Unknown Sources**
   - Go to **Settings** → **Security**
   - Toggle on **Unknown Sources** (or **Install unknown apps**)

2. **Download the APK File**
   - Visit the GitHub repository
   - Download the latest `.apk` file
   - Or visit the provided download link

3. **Install the APK**
   - Open your file manager
   - Navigate to the downloaded APK file
   - Tap the file and select **Install**
   - Grant necessary permissions

4. **Launch the App**
   - Go to **Settings** → **Apps**
   - Find "Allowance Budget Management App"
   - Tap **Open** or find it in your app drawer

### Permissions Required
- Storage access (to save budget data)
- Internet access (for cloud sync, if enabled)

---

## Installation on iOS

### Prerequisites
- iPhone/iPad running iOS 12.0 or higher
- Apple ID
- Minimum 50MB free storage

### Step-by-Step Installation

#### Method 1: Using Pythonista or Pyto
1. **Install "Pythonista" or "Pyto"** from the App Store
2. **Open the app** and create a new script
3. **Copy the code** from this GitHub repository
4. **Paste the code** into the script editor
5. **Tap the RUN button (▶️)** to execute

#### Method 2: Using App Store
- Open the **App Store** on your iPhone or iPad
- Tap the **Search** tab at the bottom
- Search for "Allowance Budget Management App"
- Tap **Get**, then **Install**
- Use Face ID, Touch ID, or Apple ID to authenticate
- Wait for the installation to complete

#### Step 2: Launch the App
- The app will appear in your home screen
- Tap the app icon to launch it
- Allow any requested permissions (storage, notifications)

#### Step 3: Grant Permissions
- **Notifications**: Allow to get budget alerts
- **Calendar**: Optional, for scheduling budget reviews
- **Health**: Not required

### Alternative: TestFlight (Beta)
If you want to test the beta version:

1. Install **TestFlight** from the App Store
2. Accept the beta invitation from the developer
3. Tap **Install** in TestFlight
4. Launch the app from TestFlight

---

## Features

### 💰 Budget Management
- Set monthly or weekly budgets
- Track budget type (Personal, Groceries, etc.)
- Real-time budget monitoring

### 📊 Expense Tracking
- Add expenses with name, amount, and date
- View detailed expense list
- Categorize expenses

### 📈 Dashboard
- Visual budget usage progress bar
- Remaining budget calculation
- Budget status warnings (Under Control / Caution / Exceeded)

### 📋 Reports
- Comprehensive expense reports
- Total expenses summary
- Remaining budget overview

---

## Usage

### Main Menu Options
1. **Set Budget**: Define your budget amount and type
2. **Expense Input Screen**: Add a new expense
3. **View Expenses**: Display all recorded expenses
4. **Budget Dashboard**: See visual budget status
5. **Report Page**: View detailed financial report
6. **Exit**: Close the application

### Example Workflow
```
1. Enter your name
2. Set Budget → Monthly, ₱5,000
3. Add Expenses → Coffee (₱100), Lunch (₱250)
4. View Dashboard → See usage: [████────────────────] 7.00%
5. View Report → Complete expense breakdown
```

---

## Troubleshooting

### PC Issues
| Problem | Solution |
|---------|----------|
| Python not found | Install Python from [python.org](https://www.python.org/downloads/) |
| ModuleNotFoundError | Ensure all dependencies are installed |
| Permission denied | Run command prompt as Administrator |

### Android Issues
| Problem | Solution |
|---------|----------|
| App won't install | Enable Unknown Sources in Settings → Security |
| App crashes | Clear app cache in Settings → Apps → Clear Cache |
| Storage error | Free up storage space on device |
| Pydroid 3 won't run code | Check Python version in Pydroid settings |

### iOS Issues
| Problem | Solution |
|---------|----------|
| Can't find in App Store | The app may still be in review; check back later |
| Installation fails | Check your Apple ID credentials |
| App crashes on launch | Restart your device and try again |
| Pythonista/Pyto won't run | Update to latest app version from App Store |

---

## System Requirements

### PC
- **OS**: Windows 10+, macOS 10.14+, or Linux (Ubuntu 18.04+)
- **Memory**: 512MB RAM minimum
- **Storage**: 100MB free space
- **Python**: 3.8 or higher

### Android
- **Version**: Android 8.0 (API 26) or higher
- **Memory**: 2GB RAM minimum
- **Storage**: 50MB free space
- **Apps**: Pydroid 3 (for direct code execution)

### iOS
- **Version**: iOS 12.0 or higher
- **Memory**: 2GB RAM minimum
- **Storage**: 50MB free space
- **Apps**: Pythonista or Pyto (for direct code execution)

---

## Data Storage

- **PC**: Data saved in `data.json` file in the application directory
- **Android**: Data saved locally in app storage
- **iOS**: Data saved locally in app storage

All data is stored offline and not uploaded unless you explicitly enable cloud sync.

---

## Support

For issues, suggestions, or bug reports:
- Open an issue on GitHub
- Contact the development team
- Check the [FAQ](#faq) section

---

## License

This project is licensed under the MIT License - see the LICENSE file for details.

---

## Version History

- **v1.0.0** (Current): Initial release
  - Basic budget management
  - Expense tracking
  - Dashboard and reports
  - Multi-platform support

---

## Contributing

We welcome contributions! Please:
1. Fork the repository
2. Create a feature branch
3. Submit a pull request

---

**Happy budgeting! 💳**

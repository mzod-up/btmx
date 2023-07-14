# BTMX: A Text-Based Bass Tab to MusicXML Converter

## About the program

BTMX is a lightweight program that is capable of generating MusicXML files from text-based bass guitar tablature. This program is fully-written in a cross-platform language—Python—and is therefore designed to be able to run on Windows, Mac, and Linux systems.

**Disclaimer:** Due to the limitations in rhythmic expression and the general lack of consistency in bass tablature, BTMX-generated MusicXML files follow the conventions of **stemless notation**—putting the focus on providing accurate translations of bass tablature notes into their standard music **pitch equivalents**, and putting less concern on approximating the actual rhythm of the music. Actual note durations and other rhythmic elements may be further added to the sheet music after importing BTMX's output MusicXML files within any compatible music sheet editing application.

---

## User Guide

### Downloading the program

1.  Open terminal in the directory BTMX is to be stored in.
2.  Run the following code to clone the repo:

    ```
    git clone https://github.com/mzod-up/btmx.git
    ```

3.  Some sample tabs may be found in the _tabs_ folder. (The file "hi.txt" contains an example of an invalid .txt file)

### Using the program

1. Open terminal in the directory where BTMX was cloned.
2. Run the following code to start up the program:

   ```
   python btmx.py
   ```

3. When program loads, click the "Import Bass Tab" button to prompt file selection.
4. Select a valid .txt file containing text-based bass tabs to import.
5. An error message will appear if the selected file does not contain valid tabs, while an import message will appear if the selected file contains valid tabs.
6. If import is successful, BTMX will generate a MusicXML file **(Format: filename.xml)** that may be found in the same directory as the selected .txt file.

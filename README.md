# BTMX: A Text-Based Bass Tab to MusicXML Converter

BTMX is a lightweight program that is capable of generating MusicXML files from text-based bass guitar tablature. This program is fully-written in a cross-platform language—Python—and is therefore designed to be able to run on Windows, Mac, and Linux systems.

**Disclaimer:** Due to the limitations in rhythmic expression and the general lack of consistency in bass tablature, BTMX-generated MusicXML files follow a **stemless notation**—placing the main focus on providing accurate translations of bass tablature notes into their standard music **pitch equivalents**, and putting less concern on approximating the actual rhythm of the music. Actual note durations and rhythm may be further adjusted after importing the output MusicXML files within any compatible music sheet editing application.

---

## User Guide

### Downloading the program

> 1. Open terminal in the directory BTMX is to be stored in.
> 2. Run the following code to clone the repo:
>    ```git
>    git clone https://github.com/mzod-up/btmx.git
>    ```

### Using the program

> 1. Open terminal in program's main directory.
> 2. Run the following code to start up the program:
>    ```
>    python btmx.py
>    ```
> 3. When program loads, click the "Import Bass Tab" button to prompt file selection.
> 4. Select a valid .txt file containing text-based bass tabs to import.
> 5. Error message will appear if selected file does not contain valid tabs.
> 6. Import message will appear if selected file contains valid tabs.
> 7. If import is successful, BTMX will generate a MusicXML file that may be found in the same directory as the selected .txt file.

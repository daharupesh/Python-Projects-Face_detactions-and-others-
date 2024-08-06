import os
import shutil
import tkinter as tk
from tkinter import filedialog, messagebox

file_types = {
    'Images': ['Artificial Intelligence', 'Bitmap Image', 'Graphics Interchange Format', 'Icon File', 'Joint Photographic Experts Group', 'JPEG Image', 'Autodesk 3ds Max', 'Wavefront Object', 'Portable Network Graphics', 'Adobe Photoshop Document', 'Scalable Vector Graphics', 'Tagged Image File Format', 'Tagged Image File Format', '3D Studio Scene', 'Rhino 3D Model'],
    'Text Files': ['Word Document', 'Word Open Document', 'OpenDocument Text', 'Outlook Message', 'Portable Document Format', 'Rich Text Format', 'LaTeX Document', 'Plain Text', 'Microsoft Works Document', 'Microsoft Works Document', 'WordPerfect Document'],
    'Executables': ['Android Application Package', 'Batch File', 'Binary File', 'Common Gateway Interface Script', 'Command File', 'Executable File', 'Java Archive', 'Python Script', 'Windows Script File', 'Jupyter Notebook'],
    'Audios': ['Audio Interchange File Format', 'Compact Disc Audio Track', 'Interchange File Format', 'MIDI File', 'MIDI File', 'MP3 Audio File', 'MPEG Audio', 'Waveform Audio File Format', 'Windows Media Audio', '3GPP2 Multimedia File', '3GPP Multimedia File'],
    'Spreadsheets': ['OpenDocument Spreadsheet', 'Microsoft Works Spreadsheet', 'Microsoft Excel', 'Microsoft Excel'],
    'Presentations': ['Apple Keynote Presentation', 'OpenDocument Presentation', 'PowerPoint Slide Show', 'PowerPoint Presentation', 'PowerPoint Presentation'],
    'Databases': ['Microsoft Access Database', 'Comma-Separated Values', 'Data File', 'Database File', 'Database File', 'Log File', 'Microsoft Database', 'Palm Database File', 'SPSS Data File', 'Structured Query Language Script', 'Tape Archive'],
    'Web Files': ['Active Server Page', 'Active Server Page Extended', 'Security Certificate', 'ColdFusion Markup Language', 'Common Gateway Interface Script', 'Perl Script', 'Cascading Style Sheet', 'HyperText Markup Language', 'JavaScript File', 'Internet Explorer Partial Download', 'Hypertext Preprocessor', 'Really Simple Syndication', 'Extensible Hypertext Markup Language'],
    'System Files': ['Backup File', 'Windows Cabinet File', 'Configuration File', 'Control Panel Item', 'Cursor Image', 'Dynamic Link Library', 'Dump File', 'Device Driver', 'Icon Image', 'Icon Image', 'Initialization File', 'Shortcut Link', 'Windows Installer Package', 'System File', 'Temporary File']
}

class FileOrganizerApp:
    def __init__(self, master):
        self.master = master
        self.master.title("File Organizer")

        self.bg_color = "#e6e6e6"
        self.text_color = "#333333"
        self.button_bg_color = "#4caf50"
        self.button_fg_color = "#ffffff"

        self.master.configure(bg=self.bg_color)

        self.path_label = tk.Label(master, text="Choose Directory:", bg=self.bg_color, fg=self.text_color)
        self.path_label.pack(pady=10)

        self.path_var = tk.StringVar()
        self.path_entry = tk.Entry(master, textvariable=self.path_var, width=50)
        self.path_entry.pack(pady=10)

        self.browse_button = tk.Button(master, text="Browse", command=self.browse_directory, bg=self.button_bg_color, fg=self.button_fg_color)
        self.browse_button.pack(pady=10)

        self.organize_button = tk.Button(master, text="Organize Files", command=self.organize_files, bg=self.button_bg_color, fg=self.button_fg_color)
        self.organize_button.pack(pady=10)

    def browse_directory(self):
        chosen_path = filedialog.askdirectory()
        self.path_var.set(chosen_path)

    def organize_files(self):
        chosen_path = self.path_var.get()

        if not chosen_path:
            messagebox.showwarning("Warning", "Please choose a directory.")
            return

        try:
            self.main(chosen_path)
            messagebox.showinfo("Success", "Files organized successfully!")
        except Exception as e:
            messagebox.showerror("Error", f"An error occurred: {e}")

def move(path, extension, file, folder_name):
    if os.path.exists(os.path.join(path, folder_name)) is False:
        os.makedirs(os.path.join(path, folder_name))

    if os.path.exists(os.path.join(path, folder_name, extension)) is False:
        os.makedirs(os.path.join(path, folder_name, extension))

    destination_path = os.path.join(path, folder_name, extension, file)

    if not os.path.exists(destination_path):
        try:
            shutil.move(os.path.join(path, file), destination_path)
            with open("moved_files.log", "a") as log_file:
                log_file.write(f"Moved: {file} to {destination_path}\n")
            return True
        except Exception as e:
            print(f'Error moving {file}: {e}')
    else:
        print(f'The destination already has a file named {file}')
    return False

def movefile(file, path):
    filename, extension = os.path.splitext(file)
    extension = extension[1:]
    extension_found = False

    for folder_name in file_types:
        if extension in file_types[folder_name]:
            extension_found = True
            return move(path, extension, file, folder_name)

    if not extension_found:
        return move(path, extension, file, 'Other')


def count_movable_item(path, files):
    total_movable_file = 0
    for file in files:
        if os.path.isfile(os.path.join(path, file)):
            total_movable_file += 1
    return total_movable_file

def count_movable_item(path, files):
    total_movable_file = 0
    for file in files:
        if os.path.isfile(os.path.join(path, file)):
            total_movable_file += 1
    return total_movable_file

def main(path):
    files = os.listdir(path)
    count = 0

    for file in files:
        if os.path.isfile(os.path.join(path, file)):
            if movefile(file, path):
                count += 1
                print(f'{count} item(s) moved successfully out of {count_movable_item(path, files)}')


if __name__ == "__main__":
    root = tk.Tk()
    app = FileOrganizerApp(root)
    root.mainloop()

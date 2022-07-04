Thanks for install ProjectNotes!

This package provides a single command (`project_notes_open`).
When the command is executed it will open the file:  
`$notes_dir_path/$PROJECT_NAME/$note_file_name`  

`ProjectNotes.sublime-settings`  
```JSON
{
  "notes_dir_path": "...",
  "note_file_name": "todo",
  "add_note_dir_to_project": true,
  "note_dir_name": "notes"
}
```

If there is no project associated with the active
window the command will not do anything.

If **notes_dir_path** is not a path to an existing
directory (example: `~/Documents/notes`), it will
default to: SUBLIME_PACKAGE_PATH/User/notes
(`~/sublime-text/Packages/User/notes`).

If **add_note_dir_to_project** is set to true the directory
containing the note will get added to the current project
with the display name defined for **note_dir_name**.

## Why?

I often find myself wanting to keep notes, lists
of links and other files related to a project, in its
own directory, *outside* the project, so i don't accidentally
commit those files to **git**.

This simple package makes that workflow seamless.

## keybinding

There is no keybinding enabled by default, I personally use
<key>Alt</key>+<key>n</key>:  
```JSON
{ "keys": ["alt+n"], "command": "project_notes_open" }
```

## contact

bug/issues/enhancements:  
https://github.com/budlime/ProjectNotes

## license

### 0BSD

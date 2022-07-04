# Copyright (c) 2022, budRich. All rights reserved.
# SPDX-License-Identifier: 0BSD

import sublime
import sublime_plugin

from os.path import isdir, isfile, expanduser, split, join, basename, splitext
from os import sep, getenv, makedirs

from typing import Optional

def tilde_prefix(target: str, use_tilde: bool):
    home: Optional[str] = getenv("HOME")
    target = expanduser(target)

    # make sure directories have a trailing slash
    if isdir(target) and target != sep and target[-1] != sep:
        target += sep

    if use_tilde and home and target.startswith(home):
        target = "~" + target[len(home) :]

    return target

def add_directory_to_project(target: str, name: str) -> None:
    win = sublime.active_window()
    project_data = win.project_data() or {}
    project_folders = project_data.get("folders") or []

    directory = tilde_prefix(target, True)[:-1]

    folder = dict(
        path=directory,
        name=name,
    )

    if all(folder["path"] != directory for folder in project_folders):
        project_data.setdefault("folders", []).append(folder)
        win.set_project_data(project_data)


class ProjectNotesOpenCommand(sublime_plugin.WindowCommand):

    def run(self):
        project_path = self.window.project_file_name()

        # current window has no associated project
        if not project_path:
            return

        settings = sublime.load_settings("ProjectNotes.sublime-settings")

        project_name, _ = splitext(basename(project_path))
        note_name = settings.setdefault("note_file_name", "todo")
        note_dir = settings.setdefault("notes_dir_path", "budlabs made me do it")
        note_dir = expanduser(note_dir)

        if not isdir(note_dir):
            note_dir = join(sublime.packages_path(), "User", "notes")

        note_path = join(note_dir, project_name, note_name)

        note_dir, _ = split(note_path)

        if not isdir(note_dir):
            makedirs(note_dir)

        if (settings.get("add_note_dir_to_project")):
            add_directory_to_project(note_dir, settings.setdefault("note_dir_name", "notes"))

        if not isfile(note_path):
            sublime.status_message("Created new buffer '" + note_path + "'")
        sublime.active_window().open_file(note_path)

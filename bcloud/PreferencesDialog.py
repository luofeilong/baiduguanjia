
# Copyright (C) 2014 LiuLang <gsushzhsosgsu@gmail.com>
# Use of this source code is governed by GPLv3 license that can be found
# in http://www.gnu.org/licenses/gpl-3.0.html

from gi.repository import GLib
from gi.repository import Gtk

from bcloud import Config
_ = Config._


class PreferencesDialog(Gtk.Dialog):

    def __init__(self, app):
        self.app = app
        super().__init__(_('Preferences'), app.window, Gtk.DialogFlags.MODAL,
                         (Gtk.STOCK_CLOSE, Gtk.ResponseType.OK))
        self.set_default_response(Gtk.ResponseType.OK)

        self.set_default_size(480, 360)
        self.set_border_width(10)

        box = self.get_content_area()

        notebook = Gtk.Notebook()
        box.pack_start(notebook, True, True, 0)

        # General Tab
        general_grid = Gtk.Grid()
        general_grid.props.halign = Gtk.Align.CENTER
        general_grid.props.column_spacing = 12
        general_grid.props.row_spacing = 5
        general_grid.props.margin_top = 5
        notebook.append_page(general_grid, Gtk.Label.new(_('General')))

        dir_label = Gtk.Label.new(_('Save To:'))
        dir_label.props.xalign = 1
        general_grid.attach(dir_label, 0, 0, 1, 1)
        dir_button = Gtk.FileChooserButton()
        dir_button.set_action(Gtk.FileChooserAction.SELECT_FOLDER)
        dir_button.set_current_folder(app.profile['save-dir'])
        dir_button.connect('file-set', self.on_dir_update)
        general_grid.attach(dir_button, 1, 0, 1, 1)

        upload_hidden_label = Gtk.Label.new(_('Upload hidden files:'))
        upload_hidden_label.props.xalign = 1
        general_grid.attach(upload_hidden_label, 0, 1, 1, 1)
        upload_hidden_switch = Gtk.Switch()
        upload_hidden_switch.props.halign = Gtk.Align.START
        upload_hidden_switch.set_tooltip_text(
                _('Also upload hidden files and folders'))
        upload_hidden_switch.set_active(self.app.profile['upload-hidden-files'])
        upload_hidden_switch.connect('notify::active',
                                     self.on_upload_hidden_switch_activate)
        general_grid.attach(upload_hidden_switch, 1, 1, 1, 1)

        notify_label = Gtk.Label.new(_('Use notification:'))
        notify_label.props.xalign = 1
        general_grid.attach(notify_label, 0, 2, 1, 1)
        notify_switch = Gtk.Switch()
        notify_switch.props.halign = Gtk.Align.START
        notify_switch.set_active(self.app.profile['use-notify'])
        notify_switch.connect('notify::active', self.on_notify_switch_activate)
        general_grid.attach(notify_switch, 1, 2, 1, 1)

        dark_theme_label = Gtk.Label.new(_('Use dark theme:'))
        dark_theme_label.props.xalign = 1
        general_grid.attach(dark_theme_label, 0, 3, 1, 1)
        dark_theme_switch = Gtk.Switch()
        dark_theme_switch.set_active(self.app.profile['use-dark-theme'])
        dark_theme_switch.connect('notify::active',
                                  self.on_dark_theme_switch_toggled)
        dark_theme_switch.props.halign = Gtk.Align.START
        general_grid.attach(dark_theme_switch, 1, 3, 1, 1)

        status_label = Gtk.Label.new(_('Use Status Icon:'))
        status_label.props.xalign = 1
        general_grid.attach(status_label, 0, 4, 1, 1)
        status_switch = Gtk.Switch()
        status_switch.set_active(self.app.profile['use-status-icon'])
        status_switch.connect('notify::active', self.on_status_switch_activate)
        status_switch.props.halign = Gtk.Align.START
        general_grid.attach(status_switch, 1, 4, 1, 1)

        avatar_label = Gtk.Label.new(_('Display Avatar:'))
        avatar_label.props.xalign = 1
        general_grid.attach(avatar_label, 0, 5, 1, 1)
        avatar_switch = Gtk.Switch()
        avatar_switch.set_active(self.app.profile['display-avatar'])
        avatar_switch.connect('notify::active', self.on_avatar_switch_activate)
        avatar_switch.props.halign = Gtk.Align.START
        general_grid.attach(avatar_switch, 1, 5, 1, 1)

        # network tab
        network_grid = Gtk.Grid()
        network_grid.props.halign = Gtk.Align.CENTER
        network_grid.props.column_spacing = 12
        network_grid.props.row_spacing = 5
        network_grid.props.margin_top = 5
        notebook.append_page(network_grid, Gtk.Label.new(_('Network')))

        stream_label = Gtk.Label.new(_('Use streaming mode:'))
        stream_label.props.xalign = 1
        network_grid.attach(stream_label, 0, 0, 1, 1)
        stream_switch = Gtk.Switch()
        stream_switch.set_active(self.app.profile['use-streaming'])
        stream_switch.connect('notify::active', self.on_stream_switch_activate)
        stream_switch.props.halign = Gtk.Align.START
        stream_switch.set_tooltip_text(
                _('Open the compressed version of videos, useful for those whose network connection is slow.'))
        network_grid.attach(stream_switch, 1, 0, 1, 1)

        concurr_label = Gtk.Label.new(_('Concurrent downloads:'))
        concurr_label.props.xalign = 1
        network_grid.attach(concurr_label, 0, 1, 1, 1)
        concurr_spin = Gtk.SpinButton.new_with_range(1, 5, 1)
        concurr_spin.set_value(self.app.profile['concurr-tasks'])
        concurr_spin.props.halign = Gtk.Align.START
        concurr_spin.connect('value-changed', self.on_concurr_value_changed)
        network_grid.attach(concurr_spin, 1, 1, 1, 1)

        segments_label = Gtk.Label.new(_('Per task:'))
        segments_label.props.xalign = 1
        network_grid.attach(segments_label, 0, 2, 1, 1)
        segments_spin = Gtk.SpinButton.new_with_range(1, 10, 1)
        segments_spin.set_value(self.app.profile['download-segments'])
        segments_spin.props.halign = Gtk.Align.START
        segments_spin.connect('value-changed', self.on_segments_value_changed)
        network_grid.attach(segments_spin, 1, 2, 1, 1)
        segments_label2 = Gtk.Label.new(_('connections'))
        segments_label2.props.xalign = 0
        network_grid.attach(segments_label2, 2, 2, 1, 1)

        retries_each = Gtk.Label.new(_('Retries each:'))
        retries_each.props.xalign = 1
        network_grid.attach(retries_each, 0, 3, 1, 1)
        retries_spin = Gtk.SpinButton.new_with_range(0, 120, 1)
        retries_spin.set_value(self.app.profile['retries-each'])
        retries_spin.connect('value-changed', self.on_retries_value_changed)
        retries_spin.props.halign = Gtk.Align.START
        retries_spin.set_tooltip_text(_('0: disable retries'))
        network_grid.attach(retries_spin, 1, 3, 1, 1)
        retries_minute_label = Gtk.Label.new(_('minutes'))
        retries_minute_label.props.xalign = 0
        network_grid.attach(retries_minute_label, 2, 3, 1, 1)

        download_timeout = Gtk.Label.new(_('Download timeout:'))
        download_timeout.props.xalign = 1
        network_grid.attach(download_timeout, 0, 4, 1, 1)
        download_timeout_spin = Gtk.SpinButton.new_with_range(10, 240, 30)
        download_timeout_spin.set_value(self.app.profile['download-timeout'])
        download_timeout_spin.props.halign = Gtk.Align.START
        download_timeout_spin.connect('value-changed',
                                      self.on_download_timeout_value_changed)
        network_grid.attach(download_timeout_spin, 1, 4, 1, 1)
        download_timeout_second = Gtk.Label.new(_('seconds'))
        download_timeout_second.props.xalign = 0
        network_grid.attach(download_timeout_second, 2, 4, 1, 1)

        download_mode_label = Gtk.Label.new(_('File exists while downloading:'))
        download_mode_label.props.xalign = 1
        network_grid.attach(download_mode_label, 0, 5, 1, 1)
        download_mode_combo = Gtk.ComboBoxText()
        download_mode_combo.append_text(_('Do Nothing'))
        download_mode_combo.append_text(_('Overwrite'))
        download_mode_combo.append_text(_('Rename Automatically'))
        download_mode_combo.set_active(self.app.profile['download-mode'])
        download_mode_combo.connect('changed', self.on_download_mode_changed)
        download_mode_combo.set_tooltip_text(
                _('What to do when downloading a file which already exists on local disk'))
        network_grid.attach(download_mode_combo, 1, 5, 2, 1)

        upload_mode_label = Gtk.Label.new(_('File exists while uploading:'))
        upload_mode_label.props.xalign = 1
        network_grid.attach(upload_mode_label, 0, 6, 1, 1)
        upload_mode_combo = Gtk.ComboBoxText()
        upload_mode_combo.append_text(_('Do Nothing'))
        upload_mode_combo.append_text(_('Overwrite'))
        upload_mode_combo.append_text(_('Rename Automatically'))
        upload_mode_combo.set_active(self.app.profile['upload-mode'])
        upload_mode_combo.set_tooltip_text(
                _('What to do when uploading a file which already exists on server'))
        upload_mode_combo.connect('changed', self.on_upload_mode_changed)
        network_grid.attach(upload_mode_combo, 1, 6, 2, 1)

        box.show_all()

    def on_dir_update(self, file_button):
        dir_name = file_button.get_filename()
        if dir_name:
            self.app.profile['save-dir'] = dir_name

    def on_upload_hidden_switch_activate(self, switch, event):
        self.app.profile['upload-hidden-files'] = switch.get_active()

    def on_notify_switch_activate(self, switch, event):
        self.app.profile['use-notify'] = switch.get_active()

    def on_dark_theme_switch_toggled(self, switch, event):
        self.app.profile['use-dark-theme'] = switch.get_active()

    def on_status_switch_activate(self, switch, event):
        self.app.profile['use-status-icon'] = switch.get_active()

    def on_avatar_switch_activate(self, switch, event):
        self.app.profile['display-avatar'] = switch.get_active()

    def on_stream_switch_activate(self, switch, event):
        self.app.profile['use-streaming'] = switch.get_active()

    def on_concurr_value_changed(self, concurr_spin):
        self.app.profile['concurr-tasks'] = concurr_spin.get_value()

    def on_segments_value_changed(self, segments_spin):
        self.app.profile['download-segments'] = segments_spin.get_value()

    def on_retries_value_changed(self, retries_spin):
        self.app.profile['retries-each'] = retries_spin.get_value()

    def on_download_timeout_value_changed(self, download_timeout_spin):
        self.app.profile['download-timeout'] = download_timeout_spin.get_value()

    def on_download_mode_changed(self, combo):
        self.app.profile['download-mode'] = combo.get_active()

    def on_upload_mode_changed(self, combo):
        self.app.profile['upload-mode'] = combo.get_active()

using System;
using System.Drawing;
using System.Windows.Forms;

namespace Port_Scanner
{
    public partial class SettingsForm : Form
    {
        private readonly SettingsManager settings;
        private readonly LanguageManager lang;

        private static readonly Color AppBg = Color.FromArgb(18, 18, 18);
        private static readonly Color PanelBg = Color.FromArgb(24, 24, 24);
        private static readonly Color PanelAltBg = Color.FromArgb(30, 30, 30);
        private static readonly Color BorderColor = Color.FromArgb(52, 52, 52);
        private static readonly Color TextColor = Color.FromArgb(240, 240, 240);
        private static readonly Color InputBg = Color.FromArgb(22, 22, 22);
        private static readonly Color ButtonBg = Color.FromArgb(36, 36, 36);
        private static readonly Color ButtonBgHover = Color.FromArgb(44, 44, 44);

        public SettingsForm(SettingsManager settings, LanguageManager lang)
        {
            InitializeComponent();
            this.settings = settings;
            this.lang = lang;

            ApplyTheme();
            ApplyLanguage();
            LoadSettings();
        }

        private void ApplyTheme()
        {
            BackColor = AppBg;
            panelHeader.BackColor = PanelBg;
            panelBody.BackColor = PanelAltBg;
            panelFooter.BackColor = PanelBg;

            lblTitle.ForeColor = TextColor;
            lblLogLevel.ForeColor = TextColor;
            lblLanguage.ForeColor = TextColor;

            comboLogLevel.BackColor = InputBg;
            comboLogLevel.ForeColor = TextColor;
            comboLogLevel.FlatStyle = FlatStyle.Flat;

            comboLanguage.BackColor = InputBg;
            comboLanguage.ForeColor = TextColor;
            comboLanguage.FlatStyle = FlatStyle.Flat;
            comboLanguage.DropDownStyle = ComboBoxStyle.DropDownList;

            StyleButton(btnSave);
            StyleButton(btnCancel);
        }

        private void StyleButton(Button btn)
        {
            btn.BackColor = ButtonBg;
            btn.ForeColor = TextColor;
            btn.FlatStyle = FlatStyle.Flat;
            btn.FlatAppearance.BorderSize = 1;
            btn.FlatAppearance.BorderColor = BorderColor;
            btn.Cursor = Cursors.Hand;
            btn.UseVisualStyleBackColor = false;
            btn.MouseEnter -= Btn_MouseEnter;
            btn.MouseLeave -= Btn_MouseLeave;
            btn.Tag = ButtonBgHover;
            btn.MouseEnter += Btn_MouseEnter;
            btn.MouseLeave += Btn_MouseLeave;
        }

        private void Btn_MouseEnter(object sender, EventArgs e)
        {
            if (sender is Button btn && btn.Tag is Color hover)
                btn.BackColor = hover;
        }

        private void Btn_MouseLeave(object sender, EventArgs e)
        {
            if (sender is Button btn)
                btn.BackColor = ButtonBg;
        }

        private void ApplyLanguage()
        {
            Text = lang.GetText("Settings");
            lblTitle.Text = lang.GetText("Settings");
            lblLogLevel.Text = lang.GetText("Log level");
            lblLanguage.Text = lang.GetText("Language");

            comboLogLevel.Items.Clear();
            comboLogLevel.Items.Add(lang.GetText("None"));
            comboLogLevel.Items.Add(lang.GetText("All"));
            comboLogLevel.Items.Add(lang.GetText("Debug"));
            comboLogLevel.Items.Add(lang.GetText("Info"));
            comboLogLevel.Items.Add(lang.GetText("Warning"));
            comboLogLevel.Items.Add(lang.GetText("Error"));
            comboLogLevel.Items.Add(lang.GetText("Fatal"));

            comboLanguage.Items.Clear();
            comboLanguage.Items.Add("English");
            comboLanguage.Items.Add("Русский");
            comboLanguage.Items.Add("日本語");
            comboLanguage.Items.Add("Deutsch");
            comboLanguage.Items.Add("Français");
            comboLanguage.Items.Add("Español");
            comboLanguage.Items.Add("中文(简体)");

            btnSave.Text = lang.GetText("Save");
            btnCancel.Text = lang.GetText("Cancel");
        }

        private void LoadSettings()
        {
            comboLogLevel.SelectedIndex = LogLevelToIndex(settings.LogLevel);

            // Определяем индекс выбранного языка
            comboLanguage.SelectedIndex = settings.Language switch
            {
                "EN" => 0,
                "RU" => 1,
                "JP" => 2,
                "DE" => 3,
                "FR" => 4,
                "ES" => 5,
                "ZH" => 6,
                _ => 0
            };
        }

        private int LogLevelToIndex(LogLevel level)
        {
            return level switch
            {
                LogLevel.None => 0,
                LogLevel.All => 1,
                LogLevel.Debug => 2,
                LogLevel.Info => 3,
                LogLevel.Warning => 4,
                LogLevel.Error => 5,
                LogLevel.Fatal => 6,
                _ => 3
            };
        }

        private LogLevel IndexToLogLevel(int index)
        {
            return index switch
            {
                0 => LogLevel.None,
                1 => LogLevel.All,
                2 => LogLevel.Debug,
                3 => LogLevel.Info,
                4 => LogLevel.Warning,
                5 => LogLevel.Error,
                6 => LogLevel.Fatal,
                _ => LogLevel.Info
            };
        }

        private void btnSave_Click(object sender, EventArgs e)
        {
            settings.LogLevel = IndexToLogLevel(comboLogLevel.SelectedIndex);

            settings.Language = comboLanguage.SelectedIndex switch
            {
                0 => "EN",
                1 => "RU",
                2 => "JP",
                3 => "DE",
                4 => "FR",
                5 => "ES",
                6 => "ZH",
                _ => "EN"
            };

            // Фиксированные размеры
            settings.FontSize = 14;
            settings.ButtonFontSize = 8;
            settings.ButtonWidth = 125;
            settings.ButtonHeight = 75;

            settings.Save();
            DialogResult = DialogResult.OK;
            Close();
        }

        private void btnCancel_Click(object sender, EventArgs e)
        {
            DialogResult = DialogResult.Cancel;
            Close();
        }
    }
}
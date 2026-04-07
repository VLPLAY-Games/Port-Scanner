using System;
using System.Drawing;
using System.Drawing.Drawing2D;
using System.Threading.Tasks;
using System.Windows.Forms;

namespace Port_Scanner
{
    public partial class Form1 : Form
    {
        private readonly SettingsManager settings;
        private readonly LanguageManager lang;
        private readonly IpHelper ipHelper;
        private readonly PortScanner portScanner;
        private readonly PingHelper pingHelper;
        private readonly ActiveDevicesScanner activeScanner;

        private string currentTask = "";
        private bool waitingInput = false;

        private static readonly Color AppBg = Color.FromArgb(18, 18, 18);
        private static readonly Color PanelBg = Color.FromArgb(24, 24, 24);
        private static readonly Color PanelAltBg = Color.FromArgb(30, 30, 30);
        private static readonly Color BorderColor = Color.FromArgb(52, 52, 52);
        private static readonly Color TextColor = Color.FromArgb(240, 240, 240);
        private static readonly Color MutedTextColor = Color.FromArgb(175, 175, 175);
        private static readonly Color InputBg = Color.FromArgb(22, 22, 22);
        private static readonly Color ButtonBg = Color.FromArgb(36, 36, 36);
        private static readonly Color ButtonBgHover = Color.FromArgb(44, 44, 44);
        private static readonly Color Accent = Color.FromArgb(84, 112, 255);

        public Form1()
        {
            InitializeComponent();
            settings = new SettingsManager();
            lang = new LanguageManager(settings.Language);
            ipHelper = new IpHelper();
            portScanner = new PortScanner();
            pingHelper = new PingHelper();
            activeScanner = new ActiveDevicesScanner();

            ApplyTheme();
            LoadSettings();
            ApplyLanguage();

            Logger.Log(LogLevel.Info, "Application started");
        }

        private void ApplyTheme()
        {
            BackColor = AppBg;
            panelLeft.BackColor = PanelBg;
            panelRight.BackColor = PanelBg;
            panelDivider.BackColor = BorderColor;
            panelTopLine.BackColor = BorderColor;
            panelBottomLine.BackColor = BorderColor;

            lblSelectOption.ForeColor = TextColor;
            lblResult.ForeColor = TextColor;
            lblFooter.ForeColor = MutedTextColor;

            txtOutput.BackColor = InputBg;
            txtOutput.ForeColor = TextColor;
            txtOutput.BorderStyle = BorderStyle.FixedSingle;
            txtOutput.ReadOnly = true;

            txtInput.BackColor = InputBg;
            txtInput.ForeColor = TextColor;
            txtInput.BorderStyle = BorderStyle.FixedSingle;

            StylePrimaryButton(btnCheckIP);
            StylePrimaryButton(btnCheckAllPorts);
            StylePrimaryButton(btnAllInfo);
            StylePrimaryButton(btnCustomTask);
            StylePrimaryButton(btnPing);
            StylePrimaryButton(btnTerminal);
            StylePrimaryButton(btnActiveDevices);

            StyleSecondaryButton(btnHelp);
            StyleSecondaryButton(btnLog);
            StyleSecondaryButton(btnClear);
            StyleSecondaryButton(btnSettings);
            StyleSecondaryButton(btnAbout);

            StyleSecondaryButton(btnNavLeft);
            StyleSecondaryButton(btnNavRight);
        }

        private void StylePrimaryButton(Button btn)
        {
            StyleButtonBase(btn, ButtonBg, ButtonBgHover);
            btn.Font = new Font("Segoe UI", 9.5F, FontStyle.Regular);
            btn.Padding = new Padding(6);
            RoundControl(btn, 12);
        }

        private void StyleSecondaryButton(Button btn)
        {
            StyleButtonBase(btn, ButtonBg, ButtonBgHover);
            btn.Font = new Font("Segoe UI", 8.5F, FontStyle.Regular);
            btn.Padding = new Padding(4);
            RoundControl(btn, 10);
        }

        private void StyleButtonBase(Button btn, Color backColor, Color hoverColor)
        {
            btn.BackColor = backColor;
            btn.ForeColor = TextColor;
            btn.FlatStyle = FlatStyle.Flat;
            btn.FlatAppearance.BorderSize = 1;
            btn.FlatAppearance.BorderColor = BorderColor;
            btn.Cursor = Cursors.Hand;
            btn.TextAlign = ContentAlignment.MiddleCenter;
            btn.UseVisualStyleBackColor = false;
            btn.MouseEnter -= Btn_MouseEnter;
            btn.MouseLeave -= Btn_MouseLeave;
            btn.Tag = hoverColor;
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

        private void RoundControl(Control control, int radius)
        {
            var rect = new Rectangle(0, 0, control.Width, control.Height);
            if (rect.Width <= 0 || rect.Height <= 0) return;
            int d = radius * 2;
            using var path = new GraphicsPath();
            path.StartFigure();
            path.AddArc(rect.X, rect.Y, d, d, 180, 90);
            path.AddArc(rect.Right - d, rect.Y, d, d, 270, 90);
            path.AddArc(rect.Right - d, rect.Bottom - d, d, d, 0, 90);
            path.AddArc(rect.X, rect.Bottom - d, d, d, 90, 90);
            path.CloseFigure();
            control.Region = new Region(path);
        }

        private void LoadSettings()
        {
            txtOutput.Font = new Font("Consolas", settings.FontSize);
            txtInput.Font = new Font("Consolas", settings.FontSize);

            var menuButtons = new[] { btnCheckIP, btnCheckAllPorts, btnAllInfo, btnCustomTask, btnPing, btnTerminal, btnActiveDevices };
            foreach (var btn in menuButtons)
            {
                btn.Font = new Font("Segoe UI", Math.Max(9f, settings.ButtonFontSize - 4), FontStyle.Regular);
                btn.Size = new Size(settings.ButtonWidth, settings.ButtonHeight);
                RoundControl(btn, 12);
            }

            var bottomButtons = new[] { btnHelp, btnLog, btnClear, btnSettings, btnAbout };
            foreach (var btn in bottomButtons)
            {
                btn.Font = new Font("Segoe UI", Math.Max(8f, settings.ButtonFontSize - 6), FontStyle.Regular);
                RoundControl(btn, 10);
            }

            Logger.SetLogLevel(settings.LogLevel);
        }

        private void ApplyLanguage()
        {
            Text = lang.GetText("Port Scanner");
            lblSelectOption.Text = lang.GetText("Select option");
            lblResult.Text = lang.GetText("Result ") + "(" + lang.GetText("Ready") + ")";

            btnCheckIP.Text = lang.GetText("Check your") + Environment.NewLine + "IP";
            btnCheckAllPorts.Text = lang.GetText("Check all") + Environment.NewLine + "ports";
            btnAllInfo.Text = lang.GetText("All info");
            btnCustomTask.Text = lang.GetText("Custom IP") + Environment.NewLine + "and ports";
            btnPing.Text = lang.GetText("Ping");
            btnTerminal.Text = lang.GetText("Terminal");
            btnActiveDevices.Text = lang.GetText("Active devices");

            btnHelp.Text = lang.GetText("Help");
            btnLog.Text = lang.GetText("Log");
            btnClear.Text = lang.GetText("Clear");
            btnSettings.Text = lang.GetText("Settings");
            btnAbout.Text = lang.GetText("About");
        }

        private void AppendOutput(string text, bool newLine = true)
        {
            if (txtOutput.InvokeRequired)
            {
                txtOutput.Invoke(new Action(() => AppendOutput(text, newLine)));
                return;
            }
            txtOutput.AppendText(text + (newLine ? Environment.NewLine : ""));
            txtOutput.ScrollToCaret();
        }

        private void ClearOutput() => txtOutput.Clear();

        private void SetTaskStatus(string status)
        {
            if (lblResult.InvokeRequired)
            {
                lblResult.Invoke(new Action(() => SetTaskStatus(status)));
                return;
            }
            lblResult.Text = lang.GetText("Result ") + "(" + lang.GetText(status) + ")";
        }

        private async void btnCheckIP_Click(object sender, EventArgs e)
        {
            SetTaskStatus("Working");
            ClearOutput();
            currentTask = "CheckIP";
            await Task.Run(() =>
            {
                var ips = ipHelper.GetAllIp();
                AppendOutput("Your IP v4 are:");
                foreach (var ip in ips.Ipv4) AppendOutput(ip);
                AppendOutput("");
                AppendOutput("Your IP v6 are:");
                foreach (var ip in ips.Ipv6) AppendOutput(ip);
            });
            SetTaskStatus("Complete");
            currentTask = "";
        }

        private async void btnCheckAllPorts_Click(object sender, EventArgs e)
        {
            SetTaskStatus("Working");
            ClearOutput();
            currentTask = "AllPorts";
            AppendOutput("Scanning all open ports on all local IPs...");
            AppendOutput("");
            var ips = ipHelper.GetAllIp().Ipv4;
            foreach (var ip in ips)
            {
                AppendOutput($"Open ports on {ip}:");
                var ports = await portScanner.ScanPortsAsync(ip, 1, 49151);
                AppendOutput(ports.Count == 0 ? "All ports are closed." : string.Join(", ", ports));
                AppendOutput("");
            }
            SetTaskStatus("Complete");
            currentTask = "";
        }

        private async void btnAllInfo_Click(object sender, EventArgs e)
        {
            SetTaskStatus("Working");
            ClearOutput();
            currentTask = "AllInfo";
            AppendOutput("All information:");
            AppendOutput("Network devices info");
            AppendOutput("");
            var ipConfig = ipHelper.GetIpConfig();
            AppendOutput(ipConfig);
            AppendOutput("");
            AppendOutput("Checking open ports...");
            var ips = ipHelper.GetAllIp().Ipv4;
            foreach (var ip in ips)
            {
                AppendOutput($"Open ports on {ip}:");
                var ports = await portScanner.ScanPortsAsync(ip, 1, 49151);
                AppendOutput(ports.Count == 0 ? "All ports are closed." : string.Join(", ", ports));
                AppendOutput("");
            }
            SetTaskStatus("Complete");
            currentTask = "";
        }

        private void btnCustomTask_Click(object sender, EventArgs e)
        {
            SetTaskStatus("Wait input");
            ClearOutput();
            currentTask = "CustomIP";
            waitingInput = true;
            AppendOutput("Enter IP address to check:", false);
            txtInput.Visible = true;
            txtInput.Focus();
        }

        private void btnPing_Click(object sender, EventArgs e)
        {
            SetTaskStatus("Wait input");
            ClearOutput();
            currentTask = "Ping";
            waitingInput = true;
            AppendOutput("Enter IP or link to ping:", false);
            txtInput.Visible = true;
            txtInput.Focus();
        }

        private void btnTerminal_Click(object sender, EventArgs e)
        {
            SetTaskStatus("Wait input");
            ClearOutput();
            currentTask = "Terminal";
            waitingInput = true;
            AppendOutput("Enter command:", false);
            txtInput.Visible = true;
            txtInput.Focus();
        }

        private void btnActiveDevices_Click(object sender, EventArgs e)
        {
            SetTaskStatus("Wait input");
            ClearOutput();
            currentTask = "ActiveDevices";
            waitingInput = true;
            AppendOutput("Enter IP with subnet mask (e.g., 192.168.1.0/24):", false);
            txtInput.Visible = true;
            txtInput.Focus();
        }

        private async void txtInput_KeyPress(object sender, KeyPressEventArgs e)
        {
            if (e.KeyChar == (char)Keys.Enter && waitingInput)
            {
                waitingInput = false;
                txtInput.Visible = false;
                string input = txtInput.Text.Trim();
                txtInput.Clear();
                AppendOutput(input);
                SetTaskStatus("Working");

                switch (currentTask)
                {
                    case "CustomIP": await HandleCustomIp(input); break;
                    case "Ping": await HandlePing(input); break;
                    case "Terminal": await HandleTerminal(input); break;
                    case "ActiveDevices": await HandleActiveDevices(input); break;
                }

                SetTaskStatus("Complete");
                currentTask = "";
                e.Handled = true;
            }
        }

        private async Task HandleCustomIp(string ip)
        {
            AppendOutput("");
            AppendOutput("Enter first port:");
            string firstPortStr = await ReadLineAsync();
            if (!int.TryParse(firstPortStr, out int firstPort))
            {
                AppendOutput("Invalid port.");
                return;
            }
            AppendOutput(firstPortStr);
            AppendOutput("Enter end port:");
            string endPortStr = await ReadLineAsync();
            if (!int.TryParse(endPortStr, out int endPort))
            {
                AppendOutput("Invalid port.");
                return;
            }
            AppendOutput(endPortStr);
            AppendOutput("");
            AppendOutput($"Scanning ports on {ip} from {firstPort} to {endPort}...");
            var ports = await portScanner.ScanPortsAsync(ip, firstPort, endPort);
            AppendOutput(ports.Count == 0 ? $"All ports are closed on {ip}" : $"Open ports: {string.Join(", ", ports)}");
        }

        private async Task HandlePing(string target)
        {
            AppendOutput($"Pinging {target}...");
            string result = await pingHelper.PingAsync(target);
            AppendOutput(result);
        }

        private async Task HandleTerminal(string command)
        {
            AppendOutput($"Executing: {command}");
            string result = await Task.Run(() => TerminalHelper.ExecuteCommand(command));
            AppendOutput(result);
        }

        private async Task HandleActiveDevices(string subnet)
        {
            AppendOutput($"Searching active devices in {subnet}...");
            var devices = await activeScanner.ScanAsync(subnet);
            if (devices.Count == 0)
            {
                AppendOutput("No active devices found.");
                return;
            }
            AppendOutput($"Found {devices.Count} active devices:");
            foreach (var dev in devices)
                AppendOutput($"IP: {dev.Ip}, MAC: {dev.Mac ?? "N/A"}, Name: {dev.Name ?? "N/A"}");
        }

        private Task<string> ReadLineAsync()
        {
            var tcs = new TaskCompletionSource<string>();
            KeyPressEventHandler handler = null;
            handler = (s, e) =>
            {
                if (e.KeyChar == (char)Keys.Enter)
                {
                    txtInput.KeyPress -= handler;
                    string line = txtInput.Text.Trim();
                    txtInput.Clear();
                    txtInput.Visible = false;
                    AppendOutput(line);
                    tcs.TrySetResult(line);
                }
            };
            txtInput.KeyPress += handler;
            txtInput.Visible = true;
            txtInput.Focus();
            return tcs.Task;
        }

        private void btnHelp_Click(object sender, EventArgs e)
        {
            ClearOutput();
            AppendOutput(settings.HelpText);
        }

        private void btnLog_Click(object sender, EventArgs e)
        {
            ClearOutput();
            AppendOutput(Logger.GetLog());
        }

        private void btnClear_Click(object sender, EventArgs e) => ClearOutput();

        private void btnSettings_Click(object sender, EventArgs e)
        {
            var settingsForm = new SettingsForm(settings, lang);
            if (settingsForm.ShowDialog() == DialogResult.OK)
            {
                lang.SetLanguage(settings.Language);
                LoadSettings();
                ApplyLanguage();
                ApplyTheme();
            }
        }

        private void btnAbout_Click(object sender, EventArgs e)
        {
            ClearOutput();
            AppendOutput(settings.AboutText);
        }
    }
}
using System;
using System.Collections.Generic;
using System.Diagnostics;
using System.IO;
using System.Linq;
using System.Management; // требуется добавление ссылки на System.Management
using System.Net;
using System.Net.NetworkInformation;
using System.Net.Sockets;
using System.Runtime.InteropServices;
using System.Text;
using System.Threading;
using System.Threading.Tasks;


namespace Port_Scanner
{
    // --------------------- Logger ---------------------
    public enum LogLevel { None = 7, All = 0, Debug = 2, Info = 3, Warning = 4, Error = 5, Fatal = 6 }

    public static class Logger
    {
        private static LogLevel currentLevel = LogLevel.Info;
        private static readonly object lockObj = new object();
        private static readonly string logFile = "report.log";

        static Logger()
        {
            if (File.Exists(logFile))
                File.Delete(logFile);
        }

        public static void SetLogLevel(LogLevel level) => currentLevel = level;

        public static void Log(LogLevel level, string message)
        {
            if ((int)level < (int)currentLevel) return;
            string timestamp = DateTime.Now.ToString("yyyy-MM-dd HH:mm:ss.fff");
            string logLine = $"{timestamp} - {level.ToString().ToUpper()} - {message}";
            lock (lockObj)
            {
                File.AppendAllText(logFile, logLine + Environment.NewLine);
            }
        }

        public static string GetLog()
        {
            if (!File.Exists(logFile)) return "Log file not found.";
            return File.ReadAllText(logFile);
        }
    }


    // --------------------- Settings ---------------------
    public class SettingsManager
    {
        public int FontSize { get; set; } = 18;
        public int ButtonFontSize { get; set; } = 18;
        public int ButtonWidth { get; set; } = 100;
        public int ButtonHeight { get; set; } = 55;
        public LogLevel LogLevel { get; set; } = LogLevel.Info;
        public string Language { get; set; } = "EN";
        public string HelpText { get; } = "Help:\n\nCheck your IP - displays all IP addresses...\nCheck all ports - displays all open ports...\nAll info - displays information about IP, ports, driver...\nCustom task - scan ports on specified IP\nLog - displays all program logs\nPing - ping site, IP or server\nTerminal - custom terminal\nActive devices - check active devices in local network";
        public string AboutText { get; } = "\n\nPort Scanner v1.0.1\nby VL_PLAY Games\ngithub.com/VLPLAY-Games/Port-Scanner";

        public SettingsManager()
        {
            FontSize = 14;
            ButtonFontSize = 9;
            ButtonWidth = 100;
            ButtonHeight = 55;
            LogLevel = LogLevel.Info;
            Language = "EN";
            Load();
        }

        public void Load()
        {
            if (!File.Exists("app.cfg")) { Save(); return; }
            foreach (var line in File.ReadAllLines("app.cfg"))
            {
                var parts = line.Split('=');
                if (parts.Length != 2) continue;
                switch (parts[0])
                {
                    case "font_size": int.TryParse(parts[1], out int fs); FontSize = fs; break;
                    case "button_font_size": int.TryParse(parts[1], out int bfs); ButtonFontSize = bfs; break;
                    case "button_width": int.TryParse(parts[1], out int bw); ButtonWidth = bw; break;
                    case "button_height": int.TryParse(parts[1], out int bh); ButtonHeight = bh; break;
                    case "loglevel": int.TryParse(parts[1], out int ll); LogLevel = (LogLevel)ll; break;
                    case "language": Language = parts[1]; break;
                }
            }
        }

        public void Save()
        {
            var lines = new[]
            {
                $"font_size={FontSize}",
                $"button_font_size={ButtonFontSize}",
                $"button_width={ButtonWidth}",
                $"button_height={ButtonHeight}",
                $"loglevel={(int)LogLevel}",
                $"language={Language}"
            };
            File.WriteAllLines("app.cfg", lines);
        }
    }

    // --------------------- Language Manager ---------------------
    public class LanguageManager
    {
        private Dictionary<string, string> translations = new Dictionary<string, string>();
        private string currentLang;

        public LanguageManager(string lang)
        {
            LoadTranslations();
            SetLanguage(lang);
        }

        private void LoadTranslations()
        {
            // Ключ: строка -> "EN|RU|JP|DE|FR|ES|ZH"
            translations["EN"] = "English";
            translations["RU"] = "Русский";
            translations["JP"] = "日本語";
            translations["DE"] = "Deutsch";
            translations["FR"] = "Français";
            translations["ES"] = "Español";
            translations["ZH"] = "中文(简体)";

            translations["Port Scanner"] =
                "Port Scanner|Порт Сканер|ポートスキャナー|Port Scanner|Scanner de ports|Escáner de puertos|端口扫描器";
            translations["Select option"] =
                "Select option|Выберите опцию|オプションを選択|Option wählen|Choisir une option|Seleccionar opción|选择选项";
            translations["Result "] =
                "Result |Результат |結果 |Ergebnis |Résultat |Resultado |结果 ";
            translations["Ready"] =
                "Ready|Готов|準備完了|Bereit|Prêt|Listo|就绪";
            translations["Working"] =
                "Working|Выполняется|処理中|Arbeitet|En cours|Trabajando|工作中";
            translations["Complete"] =
                "Complete|Выполнено|完了|Abgeschlossen|Terminé|Completado|完成";
            translations["Error"] =
                "Error|Ошибка|エラー|Fehler|Erreur|Error|错误";
            translations["Wait input"] =
                "Wait input|Ожидание ввода|入力待ち|Warte auf Eingabe|Attente saisie|Esperando entrada|等待输入";

            translations["Check your"] =
                "Check your|Проверить|確認|Prüfen|Vérifier|Verificar|检查";
            translations["Check all"] =
                "Check all|Проверить все|すべて確認|Alle prüfen|Tout vérifier|Verificar todo|检查全部";
            translations["All info"] =
                "All info|Вся информация|全情報|Alle Infos|Toutes les infos|Toda la info|全部信息";
            translations["Custom IP"] =
                "Custom IP|Кастом айпи|カスタムIP|Benutzerdef. IP|IP personnalisée|IP personalizada|自定义IP";
            translations["Ping"] =
                "Ping|Пинг|Ping|Ping|Ping|Ping|Ping";
            translations["Terminal"] =
                "Terminal|Терминал|ターミナル|Terminal|Terminal|Terminal|终端";
            translations["Active devices"] =
                "Active devices|Активные устройства|アクティブデバイス|Aktive Geräte|Appareils actifs|Dispositivos activos|活动设备";

            translations["Help"] =
                "Help|Помощь|ヘルプ|Hilfe|Aide|Ayuda|帮助";
            translations["Log"] =
                "Log|Логи|ログ|Protokoll|Journal|Registro|日志";
            translations["Clear"] =
                "Clear|Очистить|クリア|Löschen|Effacer|Limpiar|清除";
            translations["Settings"] =
                "Settings|Настройки|設定|Einstellungen|Paramètres|Configuración|设置";
            translations["About"] =
                "About|О программе|について|Über|À propos|Acerca de|关于";

            translations["Log level"] =
                "Log level|Уровень лога|ログレベル|Protokollstufe|Niveau de journal|Nivel de registro|日志级别";
            translations["Language"] =
                "Language|Язык|言語|Sprache|Langue|Idioma|语言";
            translations["None"] =
                "None|Ничего|なし|Keine|Aucun|Ninguno|无";
            translations["All"] =
                "All|Всё|すべて|Alle|Tout|Todo|全部";
            translations["Debug"] =
                "Debug|Дебаг|デバッグ|Debug|Débogage|Depuración|调试";
            translations["Info"] =
                "Info|Информация|情報|Info|Info|Información|信息";
            translations["Warning"] =
                "Warning|Предупреждения|警告|Warnung|Avertissement|Advertencia|警告";
            translations["Fatal"] =
                "Fatal|Крит. ошибки|致命的|Fatal|Fatal|Fatal|致命";
            translations["Save"] =
                "Save|Сохранить|保存|Speichern|Enregistrer|Guardar|保存";
            translations["Cancel"] =
                "Cancel|Отмена|キャンセル|Abbrechen|Annuler|Cancelar|取消";
        }

        public void SetLanguage(string lang)
        {
            currentLang = lang;
        }

        public string GetText(string key)
        {
            if (translations.TryGetValue(key, out string val))
            {
                var parts = val.Split('|');
                int index = currentLang switch
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
                if (index < parts.Length)
                    return parts[index];
            }
            return key;
        }
    }



    // --------------------- IP Helper ---------------------
    public class IpInfo
    {
        public List<string> Ipv4 { get; set; } = new List<string>();
        public List<string> Ipv6 { get; set; } = new List<string>();
    }

    public class IpHelper
    {
        public IpInfo GetAllIp()
        {
            var info = new IpInfo();
            foreach (var ni in NetworkInterface.GetAllNetworkInterfaces())
            {
                if (ni.OperationalStatus != OperationalStatus.Up) continue;
                foreach (var ua in ni.GetIPProperties().UnicastAddresses)
                {
                    if (ua.Address.AddressFamily == AddressFamily.InterNetwork)
                        info.Ipv4.Add(ua.Address.ToString());
                    else if (ua.Address.AddressFamily == AddressFamily.InterNetworkV6)
                        info.Ipv6.Add(ua.Address.ToString());
                }
            }
            return info;
        }

        public string GetIpConfig()
        {
            var sb = new StringBuilder();
            foreach (var ni in NetworkInterface.GetAllNetworkInterfaces())
            {
                sb.AppendLine($"Interface: {ni.Name} - {ni.OperationalStatus}");
                foreach (var ua in ni.GetIPProperties().UnicastAddresses)
                    sb.AppendLine($"  IP: {ua.Address}");
            }
            return sb.ToString();
        }
    }

    // --------------------- Port Scanner ---------------------
    public class PortScanner
    {
        public int ConnectionTimeoutMs { get; set; } = 250;
        public int MaxConcurrency { get; set; } = 100;

        public async Task<List<int>> ScanPortsAsync(string host, int startPort, int endPort, CancellationToken cancellationToken = default)
        {
            var openPorts = new List<int>();
            using var semaphore = new SemaphoreSlim(MaxConcurrency);
            var tasks = new List<Task>();

            IPAddress ipAddress;
            if (!IPAddress.TryParse(host, out ipAddress))
            {
 
                try
                {
                    var entry = await Dns.GetHostEntryAsync(host);
                    ipAddress = entry.AddressList[0];
                }
                catch
                {
                    return openPorts;
                }
            }

            var endPoint = new IPEndPoint(ipAddress, 0);

            for (int port = startPort; port <= endPort; port++)
            {
                cancellationToken.ThrowIfCancellationRequested();
                await semaphore.WaitAsync(cancellationToken).ConfigureAwait(false);

                int currentPort = port;
                tasks.Add(Task.Run(async () =>
                {
                    try
                    {
                        if (await IsPortOpenSocketAsync(endPoint.Address, currentPort, ConnectionTimeoutMs, cancellationToken))
                        {
                            lock (openPorts)
                                openPorts.Add(currentPort);
                        }
                    }
                    finally
                    {
                        semaphore.Release();
                    }
                }, cancellationToken));
            }

            await Task.WhenAll(tasks).ConfigureAwait(false);
            openPorts.Sort();
            return openPorts;
        }

        private async Task<bool> IsPortOpenSocketAsync(IPAddress address, int port, int timeoutMs, CancellationToken cancellationToken)
        {
            using var socket = new Socket(AddressFamily.InterNetwork, SocketType.Stream, ProtocolType.Tcp);
            try
            {
                socket.Blocking = false;
                socket.NoDelay = true;

                var endPoint = new IPEndPoint(address, port);
                var ar = socket.BeginConnect(endPoint, null, null);

                using (cancellationToken.Register(() => socket.Close()))
                {
                    var waitHandle = ar.AsyncWaitHandle;
                    var result = WaitHandle.WaitAny(new[] { waitHandle, cancellationToken.WaitHandle }, timeoutMs);

                    if (result == 0) // операция завершена
                    {
                        socket.EndConnect(ar);
                        return true;
                    }
                    // Таймаут или отмена
                    socket.Close();
                    return false;
                }
            }
            catch (SocketException)
            {
                return false;
            }
            catch (ObjectDisposedException)
            {
                // Сокет закрыт отменой
                return false;
            }
            finally
            {
                try { socket.Close(); } catch { }
            }
        }
    }


    // --------------------- Ping Helper ---------------------
    public class PingHelper
    {
        public async Task<string> PingAsync(string host)
        {
            using (var ping = new Ping())
            {
                try
                {
                    var reply = await ping.SendPingAsync(host, 5000);
                    if (reply.Status == IPStatus.Success)
                        return $"Reply from {reply.Address}: time={reply.RoundtripTime}ms";
                    else
                        return $"Ping failed: {reply.Status}";
                }
                catch (Exception ex)
                {
                    return $"Error: {ex.Message}";
                }
            }
        }
    }

    // --------------------- Active Devices Scanner ---------------------
    public class DeviceInfo
    {
        public string Ip { get; set; }
        public string Mac { get; set; }
        public string Name { get; set; }
    }

    public class ActiveDevicesScanner
    {
        public async Task<List<DeviceInfo>> ScanAsync(string subnetMask)
        {
            var devices = new List<DeviceInfo>();
            var tasks = new List<Task>();
            var semaphore = new SemaphoreSlim(50);

            string network = subnetMask;
            if (!network.Contains("/")) network += "/24";
            var (baseIp, prefixLen) = ParseSubnet(network);
            if (baseIp == null) return devices;

            int hosts = (int)Math.Pow(2, 32 - prefixLen) - 2;
            var baseBytes = baseIp.GetAddressBytes();

            for (int i = 1; i <= hosts; i++)
            {
                await semaphore.WaitAsync();
                var ipBytes = (byte[])baseBytes.Clone();
                int sum = i;
                for (int j = 3; j >= 0 && sum > 0; j--)
                {
                    ipBytes[j] += (byte)(sum % 256);
                    sum /= 256;
                }
                var ip = new IPAddress(ipBytes);
                tasks.Add(Task.Run(async () =>
                {
                    try
                    {
                        using (var ping = new Ping())
                        {
                            var reply = await ping.SendPingAsync(ip, 500);
                            if (reply.Status == IPStatus.Success)
                            {
                                string mac = GetMacAddress(ip.ToString());
                                string name = GetDeviceName(ip.ToString());
                                lock (devices) devices.Add(new DeviceInfo { Ip = ip.ToString(), Mac = mac, Name = name });
                            }
                        }
                    }
                    catch { }
                    finally { semaphore.Release(); }
                }));
            }
            await Task.WhenAll(tasks);
            return devices;
        }

        private (IPAddress, int) ParseSubnet(string subnet)
        {
            var parts = subnet.Split('/');
            if (parts.Length != 2) return (null, 0);
            if (!IPAddress.TryParse(parts[0], out var ip)) return (null, 0);
            if (!int.TryParse(parts[1], out int prefix)) return (null, 0);
            return (ip, prefix);
        }

        private string GetMacAddress(string ip)
        {
            try
            {
                var arpReply = SendArp(IPAddress.Parse(ip));
                if (arpReply != null)
                    return BitConverter.ToString(arpReply).Replace('-', ':');
            }
            catch { }
            return null;
        }

        [DllImport("iphlpapi.dll", ExactSpelling = true)]
        private static extern int SendARP(uint destIp, uint srcIp, byte[] macAddr, ref uint physicalAddrLen);

        private static byte[] SendArp(IPAddress destIp)
        {
            uint dest = BitConverter.ToUInt32(destIp.GetAddressBytes(), 0);
            byte[] mac = new byte[6];
            uint len = (uint)mac.Length;
            int res = SendARP(dest, 0, mac, ref len);
            return res == 0 ? mac : null;
        }

        private string GetDeviceName(string ip)
        {
            try
            {
                var hostEntry = Dns.GetHostEntry(ip);
                return hostEntry.HostName;
            }
            catch { return null; }
        }
    }

    // --------------------- Terminal Helper ---------------------
    public static class TerminalHelper
    {
        public static string ExecuteCommand(string command)
        {
            try
            {
                var psi = new ProcessStartInfo
                {
                    FileName = Environment.OSVersion.Platform == PlatformID.Win32NT ? "cmd.exe" : "/bin/bash",
                    Arguments = Environment.OSVersion.Platform == PlatformID.Win32NT ? $"/c {command}" : $"-c \"{command}\"",
                    RedirectStandardOutput = true,
                    UseShellExecute = false,
                    CreateNoWindow = true
                };
                using (var p = Process.Start(psi))
                {
                    string output = p.StandardOutput.ReadToEnd();
                    p.WaitForExit();
                    return output;
                }
            }
            catch (Exception ex)
            {
                return ex.Message;
            }
        }
    }
}
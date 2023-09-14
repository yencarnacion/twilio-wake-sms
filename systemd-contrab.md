If you want to run `crontab-ui` as a specific user using `systemd`, you can set up a systemd service. Here's how you can do it:

1. **Install `crontab-ui` if it isn't already installed**:

   ```bash
   sudo npm install -g crontab-ui
   ```

2. **Create a systemd service file**:

   Create a new systemd service file by opening it in a text editor:

   ```bash
   sudo emacs /etc/systemd/system/crontab-ui.service
   ```

   Then, paste in the following content:

   ```ini
   [Unit]
   Description=Crontab-UI Service
   After=network.target

   [Service]
   Type=simple
   User=yencarnacion
   ExecStart=/usr/bin/env crontab-ui
   Restart=always
   RestartSec=10
   StandardOutput=syslog
   StandardError=syslog
   SyslogIdentifier=crontab-ui

   [Install]
   WantedBy=multi-user.target   
   ```

   Make sure the path to `crontab-ui` is correct. If you're unsure about the path, you can find it using:

   ```bash
   which crontab-ui
   ```

3. **Reload the systemd manager configuration**:

   ```bash
   sudo systemctl daemon-reload
   ```

4. **Start the `crontab-ui` service**:

   ```bash
   sudo systemctl start crontab-ui.service
   ```

5. **Enable the service to start on boot**:

   ```bash
   sudo systemctl enable crontab-ui.service
   ```

6. **Check the status**:

   ```bash
   sudo systemctl status crontab-ui.service
   ```

This will ensure that `crontab-ui` runs as the user `yencarnacion` and will start on boot. Adjust the service file as needed if there are special configurations or requirements for your setup.
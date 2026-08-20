module.exports = {
  apps: [
    {
      name: 'colorpi-dashboard',
      script: 'node_modules/next/dist/bin/next',
      args: 'start',
      instances: 1,
      exec_mode: 'fork',
      cwd: '/srv/samba/share/ColorPi/src/dashboard/current',
      env: {
        NODE_ENV: 'production',
        PORT: 5000
      }
    }
  ]
};
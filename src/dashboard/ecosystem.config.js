module.exports = {
  apps: [
    {
      name: 'colorpi-dashboard',
      script: 'node_modules/next/dist/bin/next',
      args: 'start',
      instances: 'max',
      exec_mode: 'cluster',
      cwd: '/srv/samba/share/ColorPi/src/dashboard/current',
      env: {
        NODE_ENV: 'production',
        PORT: 5050
      }
    }
  ]
};
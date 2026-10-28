const common = {
    cwd: __dirname,
    script: 'main.py',
    interpreter: '../.venv/bin/python3',
    interpreter_args: '-u',
    exec_mode: 'fork',
    instances: 1,
    autorestart: true,
    restart_delay: 3000,
};

module.exports = {
    apps: [
        {
            ...common,
            name: 'colorpi-bot',
        },
    ],
};
const spawn = require("child_process").spawn;

setInterval(() => {
    const pythonProcess = spawn('python3',["main.py"]);

    pythonProcess.stdout.on('data', (data) => {
        console.log(`Python Process stdout: ${data}`);
    });

    pythonProcess.stderr.on('data', (data) => {
        console.log(`Python Process stderr: ${data}`);
    });
}, 60 * 1000 * 15);

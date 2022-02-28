const spawn = require("child_process").spawn;

// Run immediately then on a 5 minute schedule
runProcess();

setInterval(() => {
    runProcess();
}, 60 * 1000 * 5);


function runProcess() {
    const pythonProcess = spawn('venv/bin/python3',["main.py"]);

    pythonProcess.stdout.on('data', (data) => {
        console.log(`Python Process stdout: ${data}`);
    });

    pythonProcess.stderr.on('data', (data) => {
        console.log(`Python Process stderr: ${data}`);
    });
}

const spawn = require("child_process").spawn;

function runProcess() {
    let date = new Date()
    let timeoutMinutes = 5 - (date.getMinutes() % 5);
    setTimeout(runProcess, timeoutMinutes * 60 * 1000);

    const pythonProcess = spawn('venv/bin/python3',["main.py"]);

    pythonProcess.stdout.on('data', (data) => {
        console.log(`Python Process stdout: ${data}`);
    });

    pythonProcess.stderr.on('data', (data) => {
        console.log(`Python Process stderr: ${data}`);
    });
}

runProcess();

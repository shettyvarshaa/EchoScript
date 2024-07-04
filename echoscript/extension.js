const vscode = require('vscode');
const axios = require('axios');
const path = require('path');
const fs = require('fs');

/**
 * @param {vscode.ExtensionContext} context
 */
async function activate(context) {
    console.log('echoscript is now active!');

    const disposable = vscode.commands.registerCommand('echoscript.helloWorld', async function () {
        try {
            const response = await axios.get('http://localhost:8080');
            const data = response.data;

            if (data.code) {
                await createJavaFile(data.code);
                vscode.window.showInformationMessage(`Message: ${data.message}\nCode has been pasted into a new Java file.`);
            } else {
                vscode.window.showInformationMessage(data.message);
            }
        } catch (error) {
            vscode.window.showErrorMessage('Error fetching data from the backend.');
        }
    });

    context.subscriptions.push(disposable);
}

async function createJavaFile(code) {
    const workspaceFolders = vscode.workspace.workspaceFolders;

    if (!workspaceFolders || workspaceFolders.length === 0) {
        vscode.window.showErrorMessage('No workspace folder open. Please open a workspace folder first.');
        return;
    }

    const workspacePath = workspaceFolders[0].uri.fsPath;
    const javaFilePath = path.join(workspacePath, 'javaCalculator.java');

    try {
        await fs.promises.writeFile(javaFilePath, code, 'utf8');
        const document = await vscode.workspace.openTextDocument(javaFilePath);
        await vscode.window.showTextDocument(document);
        vscode.window.showInformationMessage(`Java file created at ${javaFilePath}`);
    } catch (error) {
        vscode.window.showErrorMessage(`Error creating Java file: ${error.message}`);
    }
}

function deactivate() {}

module.exports = {
    activate,
    deactivate
};
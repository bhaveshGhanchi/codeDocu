// The module 'vscode' contains the VS Code extensibility API
// Import the module and reference it with the alias vscode in your code below
const vscode = require('vscode');
const axios = require('axios');

// This method is called when your extension is activated
// Your extension is activated the very first time the command is executed

/**
 * @param {vscode.ExtensionContext} context
 */
function activate(context) {

	// Use the console to output diagnostic information (console.log) and errors (console.error)
	// This line of code will only be executed once when your extension is activated
	console.log('Congratulations, your extension "codedocument" is now active!');

	// The command has been defined in the package.json file
	// Now provide the implementation of the command with  registerCommand
	// The commandId parameter must match the command field in package.json
	
	const disposable = vscode.commands.registerCommand('codedocument.generateDocstring', async function () {
		const editor = vscode.window.activeTextEditor;
	
		if (!editor) {
		  vscode.window.showErrorMessage('No active editor found!');
		  return;
		}
	
		const selection = editor.selection;
		const selectedText = editor.document.getText(selection);
	
		if (!selectedText) {
		  vscode.window.showErrorMessage('Please select some code to generate a docstring.');
		  return;
		}
	
		try {
		  const response = await axios.post('http://127.0.0.1:8000/generate-docstring', {
			code: selectedText
		  });
	
		  const docstring = response.data.docstring;
	
		  editor.edit(editBuilder => {
			editBuilder.insert(selection.start,"/** \n"+  docstring + '*/\n');
		  });
	
		  vscode.window.showInformationMessage('Docstring added successfully!');
		} catch (err) {
		  vscode.window.showErrorMessage('Failed to fetch docstring: ' + err.message);
		}
	  });

	context.subscriptions.push(disposable);
}

// This method is called when your extension is deactivated
function deactivate() {}

module.exports = {
	activate,
	deactivate
}

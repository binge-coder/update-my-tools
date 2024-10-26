// // update-tools.ts

// const exec = async (cmd: string[]) => {
//     const process = Deno.run({
//         cmd,
//         stdout: "piped",
//         stderr: "piped",
//     });

//     const { code } = await process.status();
//     const rawOutput = await process.output();
//     const rawError = await process.stderrOutput();

//     if (code === 0) {
//         console.log(new TextDecoder().decode(rawOutput));
//     } else {
//         console.error(`Error executing ${cmd.join(" ")}`);
//         console.error(new TextDecoder().decode(rawError));
//     }

//     process.close();
// };

// // Update Bun
// await exec(["bun", "upgrade"]);

// // Update Node and npm (assumes Node and npm are installed via nvm)
// await exec(["nvm", "install", "node", "--reinstall-packages-from=node"]);
// await exec(["npm", "install", "-g", "npm"]);

// // Update pnpm
// await exec(["pnpm", "install", "-g", "pnpm"]);

// // Update Python and pip
// await exec(["pyenv", "install", "--update"]);  // If using pyenv for Python version management
// await exec(["pip", "install", "--upgrade", "pip"]);

// // Update Deno
// await exec(["deno", "upgrade"]);

// // Export to mark this as a module
// export {};

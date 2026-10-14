const bcrypt = require("bcrypt");

// JavaScript source code


// Create a salt and hash password
async function hashPassword(password) {
    const saltRounds = 10;

    const hashedPassword = await bcrypt.hash(
        password,
        saltRounds
    );

    return hashedPassword;
}

// Verify the password during login
async function verifyPassword(password, hashedPassword) {
    return await bcrypt.compare(password, hashedPassword)
}
// Server connection logic using Node.js

const express = require('express');
const mysql = require('mysql2');
const cors = require('cors');

const app = express();
app.use(cors()); // Allows frontend to request data
app.use(express.json()); // Parses incoming JSON requests

// Configure the database connection pool
const db = mysql.createPool({
    host: 'cisdbss.pcc.edu',
    user: 'CIS234A_Gooey',
    password: 'CIS234ATeammore2$',
    database: 'CIS234A_Gooey'
});
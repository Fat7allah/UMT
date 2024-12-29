const path = require('path');
const webpack = require('webpack');

module.exports = {
    entry: {
        fne: './fne/public/js/fne.js'
    },
    output: {
        filename: 'fne.bundle.js',
        path: path.resolve(__dirname, 'fne/public/dist')
    },
    module: {
        rules: [
            {
                test: /\.js$/,
                exclude: /node_modules/,
                use: {
                    loader: 'babel-loader'
                }
            }
        ]
    }
}; 
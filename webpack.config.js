const path = require("path");
const webpack = require("webpack");
const CopyWebpackPlugin = require("copy-webpack-plugin");

const Assets = [
  "bootstrap/dist/css/bootstrap.css",
  "jquery/dist/jquery.min.js",
  "bootstrap/dist/js/bootstrap.min.js",
];

module.exports = {
  entry: {
    app: "./frontend/app.js",
  },
  mode: 'production',
  output: {
    path: __dirname + "/public/",
    filename: "[name].bundle.js"
  },
  plugins: [
    new CopyWebpackPlugin(
      Assets.map(asset => {
        return {
          from: path.resolve(__dirname, `./node_modules/${asset}`),
          to: path.resolve(__dirname, "./public/vendor")
        };
      })
    )
  ]
};
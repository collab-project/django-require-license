// Copyright Collab 2012-2015

require.config({

    // The number of seconds to wait before giving up on loading a script.
    // Setting it to 0 disables the timeout. The default is 7 seconds.
    waitSeconds: 7,

    // Path mappings for module names not found directly under baseUrl.
    // The path settings are assumed to be relative to baseUrl, unless the paths
    // setting starts with a "/" or has a URL protocol in it ("like http:").
    // The path that is used for a module name should not include an extension,
    // since the path mapping could be for a directory. The path mapping code will
    // automatically add the .js extension when mapping the module name to a path.
    // If require.toUrl() is used, it will add the appropriate extension, if it is
    // for something like a text template.
    paths: {
        jquery:                     'libs/jquery.min',
        almond:                     'libs/almond',
        loglevel:                   'libs/loglevel'
    },

    // Configure the dependencies and exports for older, traditional "browser
    // globals" scripts that do not use define() to declare the dependencies
    // and set a module value.
    shim: {

        loglevel: {
            exports:    'loglevel'
        },

        almond: {
            exports:    'almond'
        }
    }
});

// Load the main app module to start the app
require(['app/main']);

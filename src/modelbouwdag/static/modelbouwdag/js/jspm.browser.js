SystemJS.config({
  baseURL: "/static/",
  paths: {
    "github:*": "jspm_packages/github/*",
    "npm:*": "jspm_packages/npm/*",
    "modelbouwdag/": "modelbouwdag/"
  }
});

const express = require("express");
const swaggerJSDoc = require("swagger-jsdoc");
const swaggerUi = require("swagger-ui-express");

// Create global app objects
const app = express();

// Swagger definition
const swaggerDefinition = {
  components: {}, // ADD THIS LINE!!!
  openapi: "3.0.1",
  info: {
    title: "BKL Test Project", // Title of the documentation
    version: "1.0.0", // Version of the app
    description: "<h2> x-api-key: 7446873594394560ee6b61db6bc96d1d1e36d59bb04118a7c30e84d6b1452bb2</h2> <h3><br>1. API 호출 시 해당 API키를 꼭 헤더 에 포함하여 보내주시면 됩니다.!<br>2.로그인 후 받은 access_token은 x-access-token 헤더 값에 추가해서 보내주시면 됩니다.!<br>3.x-user-email값은 해당 로그인 한 유저의 email값을 넣어주시면 됩니다. <br>4.protocol, domain, version은 default 값이 셋팅 되어있어 API 사용만 하시면 됩니다.", // short description of the app
  },
  servers: [ {
    url: "http://127.0.0.1:5000/v1",
    description: 'Local server'
  }],
};

const options = {
  swaggerDefinition,
  apis: ["./docs/**/*.yaml"],
};

const swaggerSpec = swaggerJSDoc(options);
app.use("/docs", swaggerUi.serve, swaggerUi.setup(swaggerSpec));

const server = app.listen(process.env.PORT || 3031, () => {
  console.log(`'Listening on port '${server.address().port}`);
});
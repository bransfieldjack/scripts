const SES = require("aws-sdk").SES;

exports.handler = (event, context, callback) => {
  const data = event;
  const Source = data.Source;
  const ToAddresses = data.ToAddresses.split(",");
  const TemplateName = data.TemplateName;

  const ses = new SES();

  var params = {
    Destination: {
      ToAddresses: ToAddresses
    },
    Source: Source,
    Template: TemplateName,
    TemplateData: `{"name":"Daniel","lastName":"Arellano"}`,
    Tags: [
      {
        Name: "STRING_VALUE",
        Value: "STRING_VALUE"
      }
    ]
  };
  ses.sendTemplatedEmail(params, function(err, data) {
    if (err) console.log(err, err.stack);
    // an error occurred
    else console.log(data); // successful response
  });
};



app.controller("DashboardCtrl", function ($scope) {
  console.log("hihi")
  $scope.dateDisplay = moment().format("MMM DD, YYYY");
  $.ajax({
    type: "GET",
    url: "./chatbot_analyze",
    data: {},
    contentType: 'application/json'
  }).done(function (data) {
    try {
      $scope.count_user = data["count_user"];
      $scope.count_message = data["count_message"];
      $scope.$apply();
      $scope.afterTalk();
      // $scope.talk("bot", text);
    } catch (e) {
      console.log("Cannot get reply from bot.");
    }
  });
});

app.config(function ($stateProvider, $urlRouterProvider) {
    $urlRouterProvider.otherwise('/');
    $stateProvider
        .state({
            url: '/dashboard',
            name: 'dashboard',
            controller: 'DashboardCtrl',
            templateUrl: "./static/app/dashboard/dashboard.html"
        })
        .state({
            url: '/',
            name: 'chatbot',
            controller: 'ChatbotCtrl',
            templateUrl: "./static/app/chatbot/chatbot.html"
        });
});

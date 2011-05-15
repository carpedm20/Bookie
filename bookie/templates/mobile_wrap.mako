<html>
    <head>
        <meta http-equiv="X-UA-Compatible" content="IE=8" />
        <title>Bookie: ${self.title()}</title>
        <meta http-equiv="X-UA-Compatible" content="IE=edge,chrome=1" />

        <link rel="stylesheet" href="http://code.jquery.com/mobile/1.0a4.1/jquery.mobile-1.0a4.1.min.css" />
        <link rel="apple-touch-icon" href="/static/images/logo.128.png" />

        <script src="http://code.jquery.com/jquery-1.5.2.min.js"></script>
        <script type="text/javascript" src="/static/js/mobile.js"></script>


        % if hasattr(self, 'header'):
            ${self.header()}
        % endif

    </head>

    <body class="ui-mobile-viewport">
        ${next.body()}
    </body>

    <script src="http://ajax.aspnetcdn.com/ajax/jquery.templates/beta1/jquery.tmpl.min.js"></script>
    <script type="text/javascript">

        $(document).bind("mobileinit", function() {
            bookie.init();
        });

        $(document).ready(function () {
            $(bookie.EVENTID).trigger(bookie.events.LOAD);
        });

    </script>
    <script src="http://code.jquery.com/mobile/1.0a4.1/jquery.mobile-1.0a4.1.min.js"></script>

</html>

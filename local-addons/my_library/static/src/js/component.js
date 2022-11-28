odoo.define('my.component', function (require) {
    "use strict";
    
    const { Component, useState } = owl; // use State hook used
    const { xml } = owl.tags;

    class MyComponent extends Component {
        static template = xml`
            <div class="bg-info text-center p-2">

                <i class="fa fa-arrow-left p-1"
                    style="cursor: pointer;"
                    t-on-click="onPrevious"> </i>

                <b t-esc="messageList[Math.abs(state.currentIndex%4)]"/>

                <i class="fa fa-arrow-right p1" 
                    style="cursor: pointer;"
                    t-on-click="onNext"> </i>

                <i class="fa fa-close p-1 float-right"
                    style="cursor: pointer;"
                    t-on-click="onRemove"> </i>

            </div>`
        // constructor to component and var
        constructor() {
            console.log('CALLED:> constructor');
            super(...arguments);
            this.messageList = [
                    
                    'Hello World',
                    'Welcome to Odoo',
                    'Odoo is awesome',
                    'You are awesome too'
            ];
            // state.currentIndex%5:= the num '5' sets expected num of items in the list.  CurrentIndex: 1 is the start position of the list.
            this.state = useState({ currentIndex: 1 });
        }

        async willStart() {
            console.log('CALLED:> willStart');
        }

        mounted() {
            console.log('CALLED:> mounted');
        }

        willPatch() {
            console.log('CALLED:> willPatch');
        }

        patched() {
            console.log('CALLED:> patched');
        }

        willUnmount() {
            console.log('CALLED:> willUnmount');
        }

        // mtds to handle events
        onRemove(ev) {
            this.destroy();
        }
        onPrevious(ev) {
            this.state.currentIndex--;
        }
        onNext(ev) {
            this.state.currentIndex++;
        }
    }

    owl.utils.whenReady().then(() => {
        const app = new MyComponent();
        app.mount(document.body);
    });

});

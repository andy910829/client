class PrintAll:
    def parse_message(self, message):
        if message.get('status') == 'OK':
            print ("\n==== student list ====")

            for stu in message.get('parameters'):
                print('\nName: {}'.format(stu.get('name')))

                for subject in stu['scores']:
                    print("  subject: {}, score: {}".format(subject, stu['scores'][subject]))

            print ("\n======================")

    def execute(self, client):
        client.send_command('show', {})
        received_message = client.wait_response()
        self.parse_message(received_message)
        
        

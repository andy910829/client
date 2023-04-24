class AddStu:
    def add_subject(self, name):
        student_info = {'name': name, 'scores': {}}

        while True:
            subject = input("  Please input a subject name or exit for ending: ")

            # if exit function
            if subject == 'exit':
                break

            # if subject is in the scores list.
            if subject in student_info['scores']:
                print('  There is a same subject in the scores, pls input other subject.\n')

            # if subject not input
            elif len(subject) == 0:
                print('  Please input subject.\n')

            elif len(subject) > 0:
                try:
                    score = input("  Please input {}'s {} score or < 0 for discarding the subject: ".format(name, subject))
                    score = float(score)
                    if score < 0:
                        break
                    student_info['scores'][subject] = score

                except:
                    print("    Wrong format with reason could not convert string to float: '{}', try again".format(score))

        print('  Add function: {}'.format(student_info))
        return student_info

    def parse_message(self, message, student_info):
        if message.get('status') == 'OK':
            print('    Add {} success'.format(student_info))

    def execute(self, client):
        name = input("  Please input a student's name or exit: ")
        
        # input student information. **subject must be input something.**
        if name != 'exit':
            student_info = self.add_subject(name)

        client.send_command('add', student_info)
        received_message = client.wait_response()

        self.parse_message(received_message, student_info)

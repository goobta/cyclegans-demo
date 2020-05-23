import argparse
import cyclegan

parser = argparse.ArgumentParser(description='Configuration for Cyclegan Demo')
parser.add_argument('-d', '--debug', action='store_true', 
                    help='run the application in debug mode.')
parser.add_argument('-p', '--port', type=int, default=8888,
                    help='which port to run the application in.')

if __name__ == '__main__':
  args = parser.parse_args()
  app = cyclegan.create_app(args)
  app.run()
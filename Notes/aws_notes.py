"""
Create profile:
aws configure --profile 'name' [then input account keys and stuff]
	profile credentials & congfig stored in c/users/'username'/.aws

profile names: personal, ntpete

To use a specific profile:
aws 'service' 'command' --profile 'name'
aws ec2 describe-instances --profile 'name'
aws elasticbeanstalk describe-environments --profile 'name'

Help:
aws help
aws help topics
aws elasticbeanstalk help
"""

# EB workflow:
# see: http://docs.aws.amazon.com/elasticbeanstalk/latest/dg/eb3-cmd-commands.html
#	 eb init --profile 'name'
#	 eb create --profile 'name'
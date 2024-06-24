import boto3

# Initialize S3 client
s3 = boto3.client('s3')

bucket_name = 'rookieprojectbucket'

# Upload files to S3 with prefixes
s3.upload_file('combine.csv', bucket_name, 'raw/combine.csv')
s3.upload_file('combine.csv', bucket_name, 'backups/combine.csv')

s3.upload_file('college_passing_unclean.csv', bucket_name, 'raw/college_passing_unclean.csv')
s3.upload_file('college_passing_unclean.csv', bucket_name, 'backups/college_passing_unclean.csv')

s3.upload_file('nfl_passing_unclean.csv', bucket_name, 'raw/nfl_passing_unclean.csv')
s3.upload_file('nfl_passing_unclean.csv', bucket_name, 'backups/nfl_passing_unclean.csv')

s3.upload_file('nfl_rushing_unclean.csv', bucket_name, 'raw/nfl_rushing_unclean.csv')
s3.upload_file('nfl_rushing_unclean.csv', bucket_name, 'backups/nfl_rushing_unclean.csv')

s3.upload_file('nfl_receiving_unclean.csv', bucket_name, 'raw/nfl_receiving_unclean.csv')
s3.upload_file('nfl_receiving_unclean.csv', bucket_name, 'backups/nfl_receiving_unclean.csv')

s3.upload_file('college_rushing_unclean.csv', bucket_name, 'raw/college_rushing_unclean.csv')
s3.upload_file('college_rushing_unclean.csv', bucket_name, 'backups/college_rushing_unclean.csv')

s3.upload_file('college_receiving_unclean.csv', bucket_name, 'raw/college_receiving_unclean.csv')
s3.upload_file('college_receiving_unclean.csv', bucket_name, 'backups/college_receiving_unclean.csv')
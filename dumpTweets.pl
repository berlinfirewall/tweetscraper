use DBI;
use strict;
use warnings; 

#open(my $dataset)
opendir (my $dir, $ARGV[0]) or die "CANNOT OPEN DIRECTORY";
while (my $file = readdir($dir)){
    if (!($file eq "." || $file eq "..")){
        print "$file\n";
        my $dbh = DBI->connect("dbi:SQLite:dbname=".$ARGV[0]."/$file", "", "");
        my $sth = $dbh->prepare("SELECT content FROM TWEETS");
        $sth->execute();

        while (my $row = $sth->fetchrow_hashref){
            print "$row->{content} \n <|endoftext|> \n";
        }
        $dbh->disconnect();
    }
}

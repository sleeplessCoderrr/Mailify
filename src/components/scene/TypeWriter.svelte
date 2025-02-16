<script lang="ts">
    export let texts: string[] = [];
    export let speed: number = 100;
    export let deleteSpeed: number = 50;
    export let loop: boolean = false;

    let displayText = "";
    let index = 0;
    let count = 0;
    let textIndex = 0;

    const typeAndDelete = async () => {
        let previousText = "";

        if(count == 0) previousText = texts[0];
        count++;

        while (textIndex < texts.length) {
            const currentText = texts[textIndex];
            displayText = "";
            index = 0;

            const commonPrefix = getCommonPrefix(previousText, currentText);
            const remainingText = currentText.slice(commonPrefix.length);

            displayText = commonPrefix;
            index = commonPrefix.length;

            while (index < currentText.length) {
                displayText += currentText[index];
                index++;
                await new Promise((resolve) => setTimeout(resolve, speed));
            }

            await new Promise((resolve) => setTimeout(resolve, 500));

            while (index > commonPrefix.length) {
                displayText = displayText.slice(0, -1);
                index--;
                await new Promise((resolve) => setTimeout(resolve, deleteSpeed));
            }

            previousText = currentText;
            textIndex++;

            if (loop && textIndex === texts.length) {
                textIndex = 0;
            }
        }
    };

    const getCommonPrefix = (str1: string, str2: string) => {
        let i = 0;
        while (i < str1.length && i < str2.length && str1[i] === str2[i]) {
            i++;
        }
        return str1.slice(0, i);
    };

    $: if (texts.length > 0) typeAndDelete();
</script>

<span>{displayText}</span>

<script lang="ts">
    import EmailLetter from "../scene/EmailLetter.svelte";
    import MailLogo from "../icon/MailIcon.svelte";
    import TypeWriter from "../scene/TypeWriter.svelte";
    import Write from "../scene/Write.svelte";

    export let texts: string[] = [];
</script>

<div class="flex-column justify-items-center">
    <div class="flex flex-row gap-4 self-center">
        <MailLogo props="size-6 self-center bg-blaze rounded p-0 stroke-stone-200"/>
        <p class="text-base my-4 font-medium">
            <TypeWriter
                texts={texts}
                speed={60}
                loop={true}
            />
        </p>
    </div>
    <p class="text-8xl my-6 font-medium text-center">
        <Write /> Email <br/> That Get Noticed
    </p>
</div>
<div class="w-full justify-items-center mt-96 mb-24">
    <EmailLetter/>
</div>
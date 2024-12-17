<script lang="ts">
    export let activeCategory: string;
</script>

<div class="flex space-x-4 mt-6 text-midnight">
    {#if activeCategory === "Applying Job"}
        <p>
            This category is for generating emails related to <b>job applications</b>. It can help you write emails expressing interest in a position, introducing yourself to potential employers, or following up on job opportunities.
        </p>
    {:else if activeCategory === "College"}
        <p>
            This category is for emails related to <b>college applications, admissions inquiries, or academic matters.</b> It can assist in writing emails to admissions offices, asking about programs, or following up on application statuses.
        </p>
    {/if}
</div>
